from pydantic import BaseModel
from datetime import date

class USerCreateSchema(BaseModel):
    username :str

    password:str

    height:float
    class Config:
        extra = "forbid"

class UserCreateWeight(BaseModel):
    weight : float
    
    class Config:
        extra = "forbid"