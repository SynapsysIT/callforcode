from fastapi import FastAPI
from api.data import data
from fastapi.middleware.cors import CORSMiddleware
# from api.models import init_measurements_model

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Spécifie explicitement le frontend
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les en-têtes
)
# # ✅ Charger le modèle au démarrage de l'API
# @app.on_event("startup")
# async def startup_event():
#     global MeasurementsModel
#     MeasurementsModel = await init_measurements_model()
#     print("✅ Modèle chargé :", MeasurementsModel.model_json_schema())
app.include_router(data)
# app.include_router(data)