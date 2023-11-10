from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import dlschemas, models, database, hash
from typing import List
from sqlalchemy.orm import Session, relationship
from ..hash import Hash
from ..respository import user

get_db = database.get_db
router = APIRouter(
    tags=["Users"],
    prefix="/user"
)

@router.post('/', response_model=dlschemas.ShowUser)
def create_user(request:dlschemas.User, db : Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=dlschemas.ShowUser)
def get_user(id:int, db:Session=Depends(get_db)):
    return user.get(id, db)