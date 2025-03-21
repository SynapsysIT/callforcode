from fastapi import FastAPI

from api.traitement import traitement

app = FastAPI()

app.include_router(traitement)
