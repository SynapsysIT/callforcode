from typing import List
from fastapi import Header, APIRouter
#from pymongo import MongoClient
from api.models import Contribute
#import requests


# mongo_user = "admin"
# mongo_password = "secretDZHAUIZDNAZDZADQLWMML1213"
# mongo_host = "callforcode.technyvue.fr"
# mongo_port = 27017
# db_name = "measurements_db_loick"
# mongo_collection = "aggregated_measurements"
# client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")

# IMB_API_KEY = "BtHADYjAU49vcBEVrreNO3UBqWqpUowBVjyULONlCuSO"
# IBM_PROJECT_ID = "f8d63044-425a-4416-9355-df29fc58ac16"
# IBM_ASSET_ID = "416386eb-240b-4db5-b695-43d7926f0b2a"
# IMB_WS_URL = f"https://dataplatform.cloud.ibm.com/projects/{IBM_PROJECT_ID}/data-assets/{IBM_ASSET_ID}/?context=wx"


contribute = APIRouter()

# @contribute.get('/', response_model=List[Contribute])
# async def index():
#     return [
#         Contribute(
#             station_id=None,
#             longitude=None,
#             latitude=None,
#             date=None,
#             chemicalElements=None,
#             prediction_potability=None,
#             non_potability_reason=None
#         )
#     ]

# @contribute.get('/', response_model=List[Contribute])
# async def index():
#     return [{
#         "station_id": "station_id",
#         "longitude": "longitude",
#         "latitude":"latitude",
#         "date":"date",
#         "chemicalElements":"chemicalElements",
#         "prediction_potability":"prediction_potability",
#         "non_potability_reason":"non_potability_reason"
#         }]

@contribute.get('/', response_model=List[Contribute])
async def index():
   tt = Contribute(titre="LOL", station_id=None,Latitude=-22.3775, Longitude=-62.523611)
   country_code = tt.get_country_from_coordinates()
   return [{
        "title": "Welcome on the generator API 1",
        "documentation": "Read the doc",
        "tt":country_code
    }]

# @contribute.post('/', status_code=201)
# async def add_data(payload: Contribute):
#     if not payload.station_id and payload.longitude and payload.latitude:
#         existing_station = payload.find_nearest_station()
#         if existing_station:
#             payload.station_id = existing_station
#         else:
#             country_code = payload.get_country_from_coordinates(payload.Latitude, payload.Longitude)
#             payload.station_id = payload.generate_station_id(country_code)
#             payload.Country_Name = country_code
#     result = payload.insert_data_mongodb()
#     return {"inserted_id": str(result.inserted_id)}

    # contribution = payload.model_dump()
    # contribution["chemicalElements"] = {f"{k}_value": v for k, v in contribution["chemicalElements"].items()}

    # prediction_potability = payload.get_prediction_potability()

    # if (contribution["longitude"] != None and contribution["latitude"] != None and contribution["station_id"] == None):
    #     pass # Recup pays avec IA (seb) et création d'un nouvel id
    

    # db_id = payload.insert_data_mongodb()

    # return {
    #     "message": "Contribution received",
    #     "db_id": db_id,
    #     "prediction_potability": prediction_potability,
    #     "debug_watson": prediction_potability
    # }


# @contribute.post('/post_photo', status_code=201)
# async def post_photo(payload: Contribute):
#     photo = payload.dict()
#     # do something
#     return {'id': 'return something'}


