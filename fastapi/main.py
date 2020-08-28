from fastapi import FastAPI
from routers.api import api

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/hello")
def hello():
    return "hello"

 
app.mount("/api/v1", api)
