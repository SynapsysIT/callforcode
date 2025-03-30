from typing import List
from fastapi import Header, APIRouter
from api.models import Generator


generator = APIRouter()



@generator.get('/')
async def index(station_id: str, language: str="English"):
   gen = Generator(station_id=station_id, language=language)
   rapport = gen.generate_rapport()
   return rapport

@generator.get('/details')
async def details(station_id: str, language: str="English"):
   station = Generator(station_id=station_id, language=language)
   details=station.generate_station_details()
   return details