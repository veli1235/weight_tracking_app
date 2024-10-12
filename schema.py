from pydantic import BaseModel

class USerCreateSchema(BaseModel):
    username :str

    password:str

    height:float
    class Config:
        extra = "forbid"