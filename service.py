from sqlalchemy.orm import Session
from schema import *
from models import User
from fastapi import HTTPException
from exception import *
import  psycopg2 
from settings import DATABASE_URL
import bcrypt


def get_user_from_db(*,username:str, db: Session):
    user = db.query(User).filter(User.username==username).first()
    if not user :
        raise UserNotFound()
    return {"username":user.username}


def create_user_in_db(data: USerCreateSchema,db:Session):
    hashed_password=bcrypt.hashpw(data.password.encode("utf-8"),bcrypt.gensalt())
    new_user=User(username=data.username,password=hashed_password.decode("utf-8"))
    user=db.query(User).filter_by(username=new_user.username).first()
    if user:
        raise UserIsExists()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"}
