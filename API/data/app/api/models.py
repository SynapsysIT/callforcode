from typing import Lis
from pydantic import BaseModel

class Data(BaseModel):
    title: str
    localisation: str
    data: Object


