
from typing import List, Dict, Optional
from pydantic import BaseModel
from pymongo import MongoClient

mongo_user = "admin"
mongo_password = "secretDZHAUIZDNAZDZADQLWMML1213"
mongo_host = "callforcode.technyvue.fr"
mongo_port = 27017
db_name = "measurements_db_loick"
mongo_collection = "aggregated_measurements"
client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")

class Contribute(BaseModel):
    station_id: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    chemicalElements: Optional[Dict[str,str]] = None
    prediction_potability: Optional[str] = None
    non_potability_reason: Optional[str] = None

    def insert_data_mongodb(self) -> str:
        try:
            client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")
            db = client[db_name]
            collection = client[mongo_collection]
        except Exception as e:
            print(f"Erreur de connexion à MongoDB: {e}")
        data = self.dict()
        result = mongo_collection.insert_one(data)
        return str(result.inserted_id)

    def get_prediction_potability(self):
        THRESHOLDS = {
            "Fluoride": (0.1, 1.5), "Cadmium": (0, 0.005), "Sodium": (0, 200), "Boron": (0, 1.5),
            "Selenium": (0, 0.04), "Nickel": (0, 0.07), "Barium": (0, 1.3), "Lead": (0, 0.01),
            "Arsenic": (0, 0.01), "Chromium": (0, 0.05), "Zinc": (0, 5), "Copper": (0, 2),
            "Mercury": (0, 0.001), "Uranium": (0, 0.03), "Aluminium": (0, 0.2), "Iron": (0, 0.3),
            "Antimony": (0, 0.02), "Cyanide": (0, 0.07), "PAH": (0, 0.0001), "Halocarbon": (0, 0.0001),
            "Phosphorus": (0, 5), "Manganese": (0, 0.4), "Potassium": (0, 100), "Bromine": (0, 1),
            "Strontium": (0, 4), "Silicon": (0, 100), "Gallium": (0, 5), "Rubidium": (0, 5),
            "Lanthanum": (0, 2), "Thallium": (0, 0.002), "Lithium": (0, 2.5), "Vanadium": (0, 0.1),
            "Magnesium": (0, 50), "Bismuth": (0, 0.1), "Molybdenum": (0, 0.07), "Tin": (0, 2),
            "Phytoplankton": (0, 10), "Dissolved_Gas": (5, 15), "Electrical_Conductance": (0, 2500),
            "Hardness": (30, 500), "pH": (6.5, 8.5), "Temperature": (0, 25)
        }

        non_potable_reasons = []
        measured_elements = 0

        if not self.chemicalElements:
            return "No chemical elements provided"

        for element, (min_thresholds, max_thresholds) in THRESHOLDS.items():
            key_value = f"{element}_value"
            key_unit = f"{element}_unit"

            if key_value in self.chemicalElements:
                measured_elements +=1
                value = self.chemicalElements[key_value]

                if self.chemicalElements[key_unit] == "µ*":
                    value /= 1000

                if min_thresholds is not None and value < min_thresholds:
                    non_potable_reasons.append(f"{element} trop bas ({value}, min {min_thresholds})")

                if max_thresholds is not None and value > max_thresholds:
                    non_potable_reasons.append(f"{element} dépasse {max_thresholds} - value : ({value})")

        if len(non_potable_reasons) > 0:
            potability_status = "Not potable"
        elif measured_elements < 5:
            potability_status = "Undetermined"
        else:
            potability_status = "Potable"

        return {
            "potability_status": potability_status, 
            "non_potable_reasons": non_potable_reasons
        }

                

    


