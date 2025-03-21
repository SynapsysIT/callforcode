from typing import List
from fastapi import Header, APIRouter

from api.models import Contribute



contribute = APIRouter()



@contribute.get('/', response_model=List[Contribute])
async def index():
   return [{

        "title": "Welcome to the contribute API",
        "documentation": "Read the doc"
    }]

@contribute.post('/', status_code=201)
async def add_data(payload: Contribute):
    contribution = payload.dict()
    # append to db
    return {'id': "ID to return"}


@contribute.post('/post_photo', status_code=201)
async def post_photo(payload: Contribute):
    photo = payload.dict()
    # do something
    return {'id': 'return something'}


