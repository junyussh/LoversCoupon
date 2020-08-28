from pydantic import BaseModel
from enum import Enum
from datetime import date
from fastapi import APIRouter, HTTPException

router = APIRouter()

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

@router.get("/register")
def registerGet():
    return "register"

@router.post("/register")
def register(user: User):
    return user
