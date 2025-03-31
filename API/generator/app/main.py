from fastapi import FastAPI

from api.generator import generator

app = FastAPI()

app.include_router(generator, prefix="/generator")

