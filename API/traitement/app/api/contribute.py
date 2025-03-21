from typing import list
from fastapi import Header, APIRouter

from api.models import Traitement



traitement = APIRoute()



@traitement.get('/', response_model=List(Contribute))
async def index():
   return {
        "title": "Contribute to the data about water quality",
        "Documentation": "Read the doc"
    }

@traitement.post('/', status_code=201)
async def add_data(payload: Contribute):
    contribution = payload.dict()
    # append to db
    return {'id': "ID to return"}


@traitement.post('/post_photo', status_code=201)
async def post_photo(payload: Contribute):
    photo = payload.dict()
    # do something
    return {'id': 'return something'}


