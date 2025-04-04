
from typing import Dict, Optional
from pydantic import BaseModel
from pymongo import MongoClient
import requests
from geopy.distance import geodesic
from api.database import MeasurementsDb



class Contribute(BaseModel):
    station_id: Optional[str] = None
    sample_date: Optional[str] = None
    Longitude: Optional[float] = None
    Latitude: Optional[float] = None
    Boron_value: Optional[float] = None
    Cadmium_value: Optional[float] = None
    Oxygen_Demand_value: Optional[float] = None
    Sulfur_value: Optional[float] = None
    Silver_value: Optional[float] = None
    Manganese_value: Optional[float] = None
    Electrical_Conductance_value: Optional[float] = None
    Selenium_value: Optional[float] = None
    Water_value: Optional[float] = None
    Nickel_value: Optional[float] = None
    Cyanide_value: Optional[float] = None
    Alkalinity_value: Optional[float] = None
    Copper_value: Optional[float] = None
    Sodium_value: Optional[float] = None
    Mercury_value: Optional[float] = None
    Magnesium_value: Optional[float] = None
    Arsenic_value: Optional[float] = None
    pH_value: Optional[float] = None
    Oxidized_Nitrogen_value: Optional[float] = None
    Iron_value: Optional[float] = None
    Optical_value: Optional[float] = None
    Potassium_value: Optional[float] = None
    Calcium_value: Optional[float] = None
    Hardness_value: Optional[float] = None
    Chloride_value: Optional[float] = None
    Lead_value: Optional[float] = None
    Other_Nitrogen_value: Optional[float] = None
    Chromium_value: Optional[float] = None
    Zinc_value: Optional[float] = None
    Potability: Optional[str] = None
    Reasons: Optional[str] = None
    Country_Name: Optional[str] = None


    def get_country_from_coordinates(self) -> str:
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={self.Latitude}&lon={self.Longitude}"
        print(url)
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            return response.json().get("address", {}).get("country", "Unknown").upper()
        return response.text
    
    def find_nearest_station(self) -> str:      
        stations = MeasurementsDb().measurements_collection.find({"Latitude": {"$ne": None}, "Longitude": {"$ne": None}})

        try:
            user_lat = float(str(self.Latitude).replace(',', '.'))
            user_lon = float(str(self.Longitude).replace(',', '.'))
        except ValueError as e:
            print(f"Erreur de conversion des coordonnées: {e}")
            return None

        for station in stations:
            try:
                station_lat = float(str(station["Latitude"]).replace(',', '.'))
                station_lon = float(str(station["Longitude"]).replace(',', '.'))
                station_coords = (station_lat, station_lon)
                
                if geodesic((user_lat, user_lon), station_coords).meters < 10:
                    return station["station_id"]
            except ValueError as e:
                print(f"Erreur de conversion pour la station {station.get('station_id', 'unknown')}: {e}")
        
        return None
    
    def generate_station_id(self) -> str:
        if not self.Country_Name:
            print("Erreur: Aucun pays spécifié pour générer l'ID de la station.")
            return None

        prefix = self.Country_Name[:3].upper()
        last_station = MeasurementsDb().measurements_collection.find_one(
            {"station_id": {"$regex": f"^{prefix}"}},
            sort=[("station_id", -1)]
        )

        if last_station and "station_id" in last_station:
            last_number = int(last_station["station_id"][3:])
            new_number = last_number + 1
        else:
            new_number = 1

        return f"{prefix}{new_number:04d}"

    def insert_data_mongodb(self) -> str:
        data = self.model_dump()
        result = MeasurementsDb().measurements_collection.insert_one(data)
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

        for element, (min_thresholds, max_thresholds) in THRESHOLDS.items():
            key = f"{element}_value"
            value = getattr(self, key, None)
        
            if value is not None:
                measured_elements += 1
                if value < min_thresholds:
                    non_potable_reasons.append(f"{element} trop bas ({value}, min {min_thresholds})")
                if value > max_thresholds:
                    non_potable_reasons.append(f"{element} dépasse {max_thresholds} - valeur : ({value})")
    

        if len(non_potable_reasons) > 0:
            potability_status = "Not potable"
        elif measured_elements < 5:
            potability_status = "Undetermined"
        else:
            potability_status = "Potable"

        return potability_status

                

    


