from typing import list
from fastapi import Header, APIRouter

from api.models import Generator


generator = APIRoute()



@generator.get('/', response_model=List(Contribute))
async def index():
   return {
        "title": "Contribute to the data about water quality",
        "Documentation": "Read the doc"
    }

@generator.post('/', status_code=201)
async def add_data(payload: Contribute):
    contribution = payload.dict()
    # append to db
    return {'id': "ID to return"}


@generator.post('/post_photo', status_code=201)
async def post_photo(payload: Contribute):
    photo = payload.dict()
    # do something
    return {'id': 'return something'}


