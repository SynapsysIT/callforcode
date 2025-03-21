from fastapi import FastAPI

from api.contribute import contribute
app = FastAPI()
app.include_router(contribute)