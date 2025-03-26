from typing import List
from fastapi import Header, APIRouter
from pymongo import MongoClient
from api.models import Contribute
import requests


mongo_user = "admin"
mongo_password = "secretDZHAUIZDNAZDZADQLWMML1213"
mongo_host = "callforcode.technyvue.fr"
mongo_port = 27017
db_name = "measurements_db_loick"
mongo_collection = "aggregated_measurements"
client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")

IMB_API_KEY = "BtHADYjAU49vcBEVrreNO3UBqWqpUowBVjyULONlCuSO"
IBM_PROJECT_ID = "f8d63044-425a-4416-9355-df29fc58ac16"
IBM_ASSET_ID = "416386eb-240b-4db5-b695-43d7926f0b2a"
IMB_WS_URL = f"https://dataplatform.cloud.ibm.com/projects/{IBM_PROJECT_ID}/data-assets/{IBM_ASSET_ID}/?context=wx"


contribute = APIRouter()

def get_ibm_token():
    url = f"https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={IMB_API_KEY}"
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None

def analyze_data_watson(data: Contribute) -> str:
    token = get_ibm_token(IMB_API_KEY)
    if not token:
        return "Error: IBM token not found"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    filtered_data = {}

    if data.station_id:
        filtered_data["station_id"] = data.station_id
    else:
        if data.longitude is not None and data.latitude is not None:
            filtered_data["longitude"] = data.longitude
            filtered_data["latitude"] = data.latitude

    if data.chemicalElements:
        filtered_data["chemicalElements"] = data.chemicalElements

    if not filtered_data:
        return "Error: No data to analyze"
    
    fields = list(filtered_data.keys())
    values = list(filtered_data.values())
    payload = {
        "fields": fields,
        "values": values
    }

    response = requests.post(IMB_WS_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["predictions"][0]
    else:
        return "Error: Prediction failed"

def insert_data_mongodb(data: dict) -> str:
    result = mongo_collection.insert_one(data)
    return str(result.inserted_id)


@contribute.get('/', response_model=List[Contribute])
async def index():
   return [{

        "title": "Welcome to the contribute API",
        "documentation": "Read the doc"
    }]

@contribute.post('/', status_code=201)
async def add_data(payload: Contribute):
    contribution = payload.model_dump()
    contribution["chemicalElements"] = {f"{k}_value": v for k, v in contribution["chemicalElements"].items()}
    prediction_potability = analyze_data_watson(payload)
    if isinstance(prediction_potability, (int, float)):  # Vérifier que c'est un nombre
        if prediction_potability == 1:
            contribution["prediction_potability"] = "Potable"
        elif prediction_potability == 0.5:
            contribution["prediction_potability"] = "Undetermined"
        elif prediction_potability == 0:
            contribution["prediction_potability"] = "Not potable"
        else:
            contribution["prediction_potability"] = f"Unknown ({prediction_potability})"
    else:
        return {
            "message": "Error in prediction",
            "db_id": "None",
            "prediction_potability": "Unknown",
            "debug_watson": prediction_potability
        }
    db_id = insert_data_mongodb(contribution)
    return {
        "message": "Contribution received",
        "db_id": db_id,
        "prediction_potability": prediction_potability,
        "debug_watson": prediction_potability
    }


@contribute.post('/post_photo', status_code=201)
async def post_photo(payload: Contribute):
    photo = payload.dict()
    # do something
    return {'id': 'return something'}


