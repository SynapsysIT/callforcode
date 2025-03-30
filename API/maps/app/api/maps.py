from typing import List
from fastapi import Header, APIRouter

from api.models import Maps
from api.map_generator import MapGenerator



maps = APIRouter()

map_generator=MapGenerator()


@maps.get('/')
async def index():
   return [{
        "title": "Welcome to the Maps API",
        "documentation": "Read the doc"
    }]


@maps.get('/generate_map/', status_code=201)
async def get_geopandas():
    map_generator.generate_map()
    return {"status": "Geopanda map generated"}


