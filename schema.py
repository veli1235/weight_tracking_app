from pydantic import BaseModel
from datetime import date

class USerCreateSchema(BaseModel):
    username :str

    password:str

    height:float
    class Config:
        extra = "forbid"

class UserCreateWeight(BaseModel):
    username : str
    datetime : date
    class Config:
        extra = "forbid"