from fastapi import FastAPI
from routers.api import users

api = FastAPI()

@api.get("/")
def read_sub():
    return {"message": "Hello World from sub API"}

@api.get("/register")
def register():
    return "register"

api.include_router(
    users.router,
    prefix="/users",
    tags=["User"]
)