from typing import List
from fastapi import Header, APIRouter

from api.models import Generator


generator = APIRouter()



@generator.get('/', response_model=List[Generator])
async def index():
   return [{
        "title": "Welcome on the generator API",
        "documentation": "Read the doc"
    }]

