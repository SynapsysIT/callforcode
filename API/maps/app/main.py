from fastapi import FastAPI

from api.maps import maps

app = FastAPI()

app.include_router(maps)
