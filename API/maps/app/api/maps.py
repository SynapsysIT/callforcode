from typing import List
from fastapi import Header, APIRouter

from api.models import Maps



maps = APIRouter()



@maps.get('/', response_model=List[Maps])
async def index():
   return {
        "title": "Contribute to the data about water quality",
        "Documentation": "Read the doc"
    }

@maps.post('/', status_code=201)
async def add_data(payload: Maps):
    contribution = payload.dict()
    # append to db
    return {'id': "ID to return"}


@maps.post('/post_photo', status_code=201)
async def post_photo(payload: Maps):
    photo = payload.dict()
    # do something
    return {'id': 'return something'}


