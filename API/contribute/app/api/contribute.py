from typing import List
from fastapi import Header, APIRouter
from pymongo import MongoClient
from api.models import Contribute
import requests


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

