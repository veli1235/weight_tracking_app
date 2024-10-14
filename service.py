from sqlalchemy.orm import Session
from schema import *
from models import User, Weight
from fastapi import HTTPException
from exception import *
import  psycopg2 
from settings import DATABASE_URL
import bcrypt


def get_user_from_db(*,username:str, db: Session):
    user = db.query(User).filter(User.username==username).first()
    if not user:
        raise UserNotFound()
    lst = []
    weights = db.query(Weight).filter_by(username=user.username,weight=Weight.weight).all()
    lst.append(weights)
    last_entry = lst[0][-1]
    return {"username":user.username,"weight":last_entry.weight}


def create_user_in_db(data: USerCreateSchema,db:Session):
    hashed_password=bcrypt.hashpw(data.password.encode("utf-8"),bcrypt.gensalt())
    new_user=User(username=data.username,password=hashed_password.decode("utf-8"),height=data.height)
    user=db.query(User).filter_by(username=new_user.username).first()
    if user:
        raise UserIsExists()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"}


def create_weight_in_db(*,username:str,data : UserCreateWeight, db : Session):
    new_weight = Weight(username = username,weight = data.weight,datetime = data.datetime)
    user = db.query(User).filter(User.username == new_weight.username).first()
    if  not user:
        raise UserNotFound()
    db.add(new_weight)
    db.commit()
    db.refresh(new_weight)
    return {"msg":"new weight is added"}

def get_weight_change_from_db(*,username:str, db: Session):
    user = db.query(Weight).filter(Weight.username==username).first()
    if not user:
        raise UserNotFound()
    lst = []
    weights = db.query(Weight).filter_by(username=user.username,weight=Weight.weight).all()
    lst.append(weights)
    last_entry = lst[0][-1]
    if len(lst[0])!=1:
        first_entry = lst[0][0].weight
    else:
        raise HTTPException(status_code=404,detail="User entered only one weight")
    return {"difference":abs(last_entry.weight-first_entry)}


def calculate_bmi_for_last_weight(*,username:str, db: Session):
    user = db.query(User).filter(User.username==username).first()
    if not user:
        raise UserNotFound()
    lst = []
    weights = db.query(Weight).filter_by(username=user.username,weight=Weight.weight).all()
    lst.append(weights)
    last_entry = lst[0][-1]
    heights= db.query(User).filter_by(username = user.username, height = User.height).first()
    height1 = heights.height
    return  {"bmi":last_entry.weight/height1**2} 
    