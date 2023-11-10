from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import dlschemas, models, database, hash
from typing import List
from sqlalchemy.orm import Session, relationship
from ..hash import Hash


def create(request:dlschemas.User, db:Session):
    new_user = models.User(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"USER WITH THE ID OF {id} NOT FOUND")
    return user