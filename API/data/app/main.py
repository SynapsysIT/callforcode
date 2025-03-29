from fastapi import FastAPI
from api.data import data
# from api.models import init_measurements_model

app = FastAPI()

# # ✅ Charger le modèle au démarrage de l'API
# @app.on_event("startup")
# async def startup_event():
#     global MeasurementsModel
#     MeasurementsModel = await init_measurements_model()
#     print("✅ Modèle chargé :", MeasurementsModel.model_json_schema())

app.include_router(data)
