from sqlalchemy import Column,Integer,String,Date,Float
from db import Base,engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    password = Column(String)
    height = Column(Float)

class Weight(Base):
    __tablename__ = "weight_entries"
    id = Column(Integer,primary_key = True)
    username = Column(String, primary_key = True)
    weight = Column(Integer)
    datetime = Column(Date)

Base.metadata.create_all(bind=engine)