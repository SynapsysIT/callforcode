from typing import List
from pydantic import BaseModel

class Traitement(BaseModel):
    title: str
    documentation: str
#    data: Object


