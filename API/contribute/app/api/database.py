from pymongo import MongoClient

class MeasurementsDb:
    def __init__(self):
        # Define the MongoDB connection parameters

        self.mongo_user = "admin"
        self.mongo_password = "secretDZHAUIZDNAZDZADQLWMML1213"
        self.mongo_host = "callforcode.technyvue.fr"
        self.mongo_port = 27017
        self.mongo_db = "measurements_db_loick"

        self.client = MongoClient(f"mongodb://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}:{self.mongo_port}/{self.mongo_db}?authSource=admin")
        self.db = self.client[self.mongo_db]

    # Define the name of the new aggregated collection
        self.aggregated_collection_name = "aggregated_measurements"

        self.measurements_collection = self.db[self.aggregated_collection_name]


class StationDb:
    def __init__(self):
        # Define the MongoDB connection parameters

        self.mongo_user = "admin"
        self.mongo_password = "secretDZHAUIZDNAZDZADQLWMML1213"
        self.mongo_host = "callforcode.technyvue.fr"
        self.mongo_port = 27017
        self.mongo_db = "measurements_db_loick"

        self.client = MongoClient(f"mongodb://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}:{self.mongo_port}/{self.mongo_db}?authSource=admin")
        self.db = self.client[self.mongo_db]

    # Define the name of the new aggregated collection
        self.station_collection_name = "GEMStat_station_metadata"

        self.station_collection = self.db[self.station_collection_name]
    def create_geo_index(self):
        """
        Créer un index géospatial 2dsphere sur le champ `location`
        """
        self.station_collection.create_index([("location", "2dsphere")])
        print("Index géospatial créé avec succès sur le champ 'location'.")