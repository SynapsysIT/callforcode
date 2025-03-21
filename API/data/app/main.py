from fastapi import FastAPI

from api.data import data

app = FastAPI()

app.include_router(data)
