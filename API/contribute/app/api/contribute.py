from typing import List
from fastapi import Header, APIRouter
from pymongo import MongoClient
from api.models import Contribute
import requests


# mongo_user = "admin"
# mongo_password = "secretDZHAUIZDNAZDZADQLWMML1213"
# mongo_host = "callforcode.technyvue.fr"
# mongo_port = 27017
# db_name = "measurements_db_loick"
# mongo_collection = "aggregated_measurements"
# client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")
# db = client[db_name]
# collection = db[mongo_collection]

# IMB_API_KEY = "BtHADYjAU49vcBEVrreNO3UBqWqpUowBVjyULONlCuSO"
# IBM_PROJECT_ID = "f8d63044-425a-4416-9355-df29fc58ac16"
# IBM_ASSET_ID = "416386eb-240b-4db5-b695-43d7926f0b2a"
# IMB_WS_URL = f"https://dataplatform.cloud.ibm.com/projects/{IBM_PROJECT_ID}/data-assets/{IBM_ASSET_ID}/?context=wx"


contribute = APIRouter()

@contribute.get('/')
async def index():
    return {
        "message": "Welcome to the API",
        "documentation": "Read the doc",
        "version": "1.0.0"
    }


@contribute.post('/', status_code=201)
def add_data(payload: Contribute):
    if not payload.station_id and payload.Longitude and payload.Latitude:
        existing_station = payload.find_nearest_station()
        if existing_station:
            payload.station_id = existing_station
        else:
            country_code = payload.get_country_from_coordinates(payload.Latitude, payload.Longitude)
            payload.station_id = payload.generate_station_id(country_code)
            payload.Country_Name = country_code

    contribution = payload.model_dump()

    payload.Potability = payload.get_prediction_potability()

    if (contribution["Longitude"] != None and contribution["Latitude"] != None and contribution["station_id"] == None):
        contribution["station_id"] = payload.find_nearest_station()
    if contribution["station_id"] == None:
        if payload.Country_Name == None:
            payload.Country_Name = payload.get_country_from_coordinates()
        contribution["station_id"] = payload.generate_station_id(payload.Country_Name)

    db_id = payload.insert_data_mongodb()

    return {
        "message": "Contribution received",
        "db_id": "db_id",
        "prediction_potability": payload.Potability,
        "dump": payload
   }

