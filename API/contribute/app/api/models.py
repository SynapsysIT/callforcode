
from typing import Dict, Optional
from pydantic import BaseModel
# from pymongo import MongoClient
# import requests
# from geopy.distance import geodesic


class Contribute(BaseModel):
    title: str
    documentation: str






# mongo_user = "admin"
# mongo_password = "secretDZHAUIZDNAZDZADQLWMML1213"
# mongo_host = "callforcode.technyvue.fr"
# mongo_port = 27017
# db_name = "measurements_db_loick"
# mongo_collection = "aggregated_measurements"
# client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")

# class Contribute(BaseModel):
#     station_id: Optional[str] = None
#     sample_date: Optional[str] = None
#     Longitude: Optional[float] = None
#     Latitude: Optional[float] = None
#     Boron_value: Optional[float] = None
#     Cadmium_value: Optional[float] = None
#     Oxygen_Demand_value: Optional[float] = None
#     Sulfur_value: Optional[float] = None
#     Silver_value: Optional[float] = None
#     Manganese_value: Optional[float] = None
#     Electrical_Conductance_value: Optional[float] = None
#     Selenium_value: Optional[float] = None
#     Water_value: Optional[float] = None
#     Nickel_value: Optional[float] = None
#     Cyanide_value: Optional[float] = None
#     Alkalinity_value: Optional[float] = None
#     Copper_value: Optional[float] = None
#     Sodium_value: Optional[float] = None
#     Mercury_value: Optional[float] = None
#     Magnesium_value: Optional[float] = None
#     Arsenic_value: Optional[float] = None
#     pH_value: Optional[float] = None
#     Oxidized_Nitrogen_value: Optional[float] = None
#     Iron_value: Optional[float] = None
#     Optical_value: Optional[float] = None
#     Potassium_value: Optional[float] = None
#     Calcium_value: Optional[float] = None
#     Hardness_value: Optional[float] = None
#     Chloride_value: Optional[float] = None
#     Lead_value: Optional[float] = None
#     Other_Nitrogen_value: Optional[float] = None
#     Chromium_value: Optional[float] = None
#     Zinc_value: Optional[float] = None
#     Potability: Optional[str] = None
#     Reasons: Optional[str] = None
#     Country_Name: Optional[str] = None

#     def get_country_from_coordinates(self) -> str:
#         response = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={self.Latitude}&lon={self.Longitude}")
#         if response.status_code == 200:
#             return response.json().get("address", {}).get("country_code", "UNK").upper()
#         return "UNK"
    
#     def find_nearest_station(self) -> str:
#         try:
#             client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")
#             db = client[db_name]
#             collection = db[mongo_collection]
#         except Exception as e:
#             print(f"Erreur de connexion à MongoDB: {e}")
#         stations = collection.find({"Latitude": {"$ne": None}, "Longitude": {"$ne": None}})
#         for station in stations:
#             station_coords = (station["Latitude"], station["Longitude"])
#             if geodesic((self.Latitude, self.Longitude), station_coords).meters < 10:
#                 return station["station_id"]
#         return None
    
#     def generate_station_id(self) -> str:
#         try:
#             client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")
#             db = client[db_name]
#             collection = db[mongo_collection]
#         except Exception as e:
#             print(f"Erreur de connexion à MongoDB: {e}")
#         count = collection.count_documents({"Country_Name": self.Country_Name}) + 1
#         return f"{self.Country_Name[:3].upper()}{count:04d}"

#     def insert_data_mongodb(self) -> str:
#         try:
#             client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}?authSource=admin")
#             db = client[db_name]
#             collection = db[mongo_collection]
#         except Exception as e:
#             print(f"Erreur de connexion à MongoDB: {e}")
#         data = self.model_dump()
#         result = collection.insert_one(data)
#         return str(result.inserted_id)

#     def get_prediction_potability(self):
#         THRESHOLDS = {
#             "Fluoride": (0.1, 1.5), "Cadmium": (0, 0.005), "Sodium": (0, 200), "Boron": (0, 1.5),
#             "Selenium": (0, 0.04), "Nickel": (0, 0.07), "Barium": (0, 1.3), "Lead": (0, 0.01),
#             "Arsenic": (0, 0.01), "Chromium": (0, 0.05), "Zinc": (0, 5), "Copper": (0, 2),
#             "Mercury": (0, 0.001), "Uranium": (0, 0.03), "Aluminium": (0, 0.2), "Iron": (0, 0.3),
#             "Antimony": (0, 0.02), "Cyanide": (0, 0.07), "PAH": (0, 0.0001), "Halocarbon": (0, 0.0001),
#             "Phosphorus": (0, 5), "Manganese": (0, 0.4), "Potassium": (0, 100), "Bromine": (0, 1),
#             "Strontium": (0, 4), "Silicon": (0, 100), "Gallium": (0, 5), "Rubidium": (0, 5),
#             "Lanthanum": (0, 2), "Thallium": (0, 0.002), "Lithium": (0, 2.5), "Vanadium": (0, 0.1),
#             "Magnesium": (0, 50), "Bismuth": (0, 0.1), "Molybdenum": (0, 0.07), "Tin": (0, 2),
#             "Phytoplankton": (0, 10), "Dissolved_Gas": (5, 15), "Electrical_Conductance": (0, 2500),
#             "Hardness": (30, 500), "pH": (6.5, 8.5), "Temperature": (0, 25)
#         }

#         non_potable_reasons = []
#         measured_elements = 0

#         if not self.chemicalElements:
#             return "No chemical elements provided"

#         for element, (min_thresholds, max_thresholds) in THRESHOLDS.items():
#             key_value = f"{element}_value"
#             key_unit = f"{element}_unit"

#             if key_value in self.chemicalElements:
#                 measured_elements +=1
#                 value = self.chemicalElements[key_value]

#                 if self.chemicalElements[key_unit] == "µ*":
#                     value /= 1000

#                 if min_thresholds is not None and value < min_thresholds:
#                     non_potable_reasons.append(f"{element} trop bas ({value}, min {min_thresholds})")

#                 if max_thresholds is not None and value > max_thresholds:
#                     non_potable_reasons.append(f"{element} dépasse {max_thresholds} - value : ({value})")

#         if len(non_potable_reasons) > 0:
#             potability_status = "Not potable"
#         elif measured_elements < 5:
#             potability_status = "Undetermined"
#         else:
#             potability_status = "Potable"

#         return {
#             "potability_status": potability_status, 
#             "non_potable_reasons": non_potable_reasons
#         }

                

    


