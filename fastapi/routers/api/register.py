from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from routers.api import api

class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'

class User(BaseModel):
    id: str
    name: str
    email: str
    password: str
    birth: date
    sex: Gender
    phone: str = None

@api.get("/register")
def register():
    return "register"