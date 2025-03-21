from typing import list
from fastapi import Header, APIRouter

from api.models import Data



data = APIRoute()



@contribute.get('/', response_model=List(Data))
async def index():
   return {
        "title": "Contribute to the data about water quality",
        "Documentation": "Read the doc"
    }

@data.post('/', status_code=201)
async def add_data(payload: Data):
    contribution = payload.dict()
    # append to db
    return {'id': "ID to return"}


@data.post('/post_photo', status_code=201)
async def post_photo(payload: Data):
    photo = payload.dict()
    # do something
    return {'id': 'return something'}


