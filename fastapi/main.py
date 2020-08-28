from fastapi import FastAPI
from routers.api import api

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.mount("/api/v1", api)
