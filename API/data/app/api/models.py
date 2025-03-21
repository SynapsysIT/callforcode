from typing import List
from pydantic import BaseModel

class Data(BaseModel):
    title: str
    documentation: str
    #data: Object


