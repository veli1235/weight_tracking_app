from pydantic import BaseModel

class USerCreateSchema(BaseModel):
    username :str

    password:str

    height:str
    class Config:
        extra = "forbid"