from typing import Lis
from pydantic import BaseModel

class Generator(BaseModel):
    title: str
    localisation: str
    data: Object


