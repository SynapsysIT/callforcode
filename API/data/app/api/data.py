from fastapi import APIRouter, HTTPException
from api.database import MeasurementsDb, StationDb
import math

data = APIRouter()

def clean_document(doc):
    """Remplace NaN, inf et -inf par None dans un dictionnaire MongoDB."""
    for key, value in doc.items():
        if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
            doc[key] = None  # ✅ JSON-compatible
    return doc


@data.get("/stations/{results_nb}")
async def get_stations(results_nb: int):
    stations = list(MeasurementsDb().measurements_collection.find().limit(results_nb))
    for station in stations:
        station["_id"] = str(station["_id"])  # Convertir ObjectId en string
        clean_document(station)  # Nettoyer NaN/inf dans le document
    return stations


@data.get('/stations_meta/')
async def get_station_meta(): 
    stations = list(StationDb().station_collection.find().limit(100))
    for station in stations:
        station["_id"] = str(station["_id"])  # Convertir ObjectId en string
        clean_document(station)  # Nettoyer NaN/inf dans le document
    return stations


@data.get('/station/{station_id}')
async def get_station_info(station_id: str): 
    station = StationDb().station_collection.find_one({"station_id": station_id})
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    station["_id"] = str(station["_id"])
    clean_document(station)  # Nettoyer NaN/inf dans le document
    return station

@data.get('/get_closest_stations/')
async def get_closest_stations(lat: str, lon: str, max_distance: int = 5000):
    try:
        # Convertir lat/lon en float, remplacer la virgule par un point
        lat = float(lat.replace(",", "."))
        lon = float(lon.replace(",", "."))
        max_distance = max_distance * 1000  # Converti distance en km en m
    except ValueError:
        raise HTTPException(status_code=404, detail="Latitude and longitude must be valid numbers.")

    # Recherche des stations proches avec la requête géospatiale
    nearby_stations = StationDb().station_collection.find({
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]  # Longitude en premier !
                },
                "$maxDistance": max_distance  # Distance max en mètres
            }
        }
    })

    results = []
    for station in nearby_stations:
        station["_id"] = str(station["_id"])  # Convertir ObjectId en string
        clean_document(station)  # Nettoyer NaN/inf dans le document
        results.append(station)

    if not results:
        raise HTTPException(status_code=404, detail="Aucune station trouvée à proximité.")

    return {"nb": len(results), "results": results}


@data.get('/get_station_measurements/{station_id}')
async def get_station_measurements(station_id: str):
    station_measurements = list(MeasurementsDb().measurements_collection.find({"station_id": station_id}))
    if not station_measurements:
        raise HTTPException(status_code=404, detail="Station measurements not found")
    for station in station_measurements:
        station["_id"] = str(station["_id"])  # Convertir ObjectId en string
        clean_document(station)  # Nettoyer NaN/inf dans le document

    return {"nb": len(station_measurements), "station_measurements": station_measurements}


@data.get('/get_stations_last_infos/{station_id}/')
async def get_station_last_info(station_id: str):
    station_last_info_list = list(MeasurementsDb().measurements_collection.find({"station_id": station_id}))
    station_info_list = station_last_info_list[len(station_last_info_list) - 10:]
    if not station_info_list:
        raise HTTPException(statu_code=404, detail='Station last infos not found')
    
    for station in station_info_list:
        station['_id']= str(station['_id'])
        clean_document(station)        

    return station_info_list