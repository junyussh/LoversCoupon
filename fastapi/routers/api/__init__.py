from fastapi import FastAPI
from routers.api import users, register

api = FastAPI()


@api.get("/")
def read_sub():
    return {"message": "Hello World from sub API"}


api.include_router(register.router)
api.include_router(
    users.router,
    prefix="/users",
    tags=["User"]
)
