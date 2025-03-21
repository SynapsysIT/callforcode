from typing import List
from pydantic import BaseModel

class Generator(BaseModel):
    title: str
    documentation: str
   # data: Object


