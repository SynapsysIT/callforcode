from typing import List
from pydantic import BaseModel

class Traitement(BaseModel):
    title: str
    localisation: str
#    data: Object


