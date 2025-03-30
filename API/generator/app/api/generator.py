from typing import List
from fastapi import Header, APIRouter

from api.models import Generator


generator = APIRouter()



@generator.get('/')
async def index():
   gen = Generator(station_id="ARG00006", language="French")
   rapport = gen.generate_rapport()
   return rapport

