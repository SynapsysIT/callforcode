
from typing import List, Dict, Optional
from pydantic import BaseModel

class Contribute(BaseModel):
    title: str
    documentation: str
    station_id: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    chemicalElements: Optional[Dict[str,str]] = None
    prediction_potability: Optional[str] = None

    


