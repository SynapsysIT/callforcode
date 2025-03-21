from typing import List
from fastapi import Header, APIRouter

from api.models import Traitement



traitement = APIRouter()



@traitement.get('/', response_model=List[Traitement])
async def index():
   return [{
        "title": "Welcome to the Traitement API",
        "documentation": "Read the doc"
    }]

@traitement.post('/', status_code=201)
async def add_data(payload: Traitement):
    contribution = payload.dict()
    # append to db
    return {'id': "ID to return"}


@traitement.post('/post_photo', status_code=201)
async def post_photo(payload: Traitement):
    photo = payload.dict()
    # do something
    return {'id': 'return something'}


