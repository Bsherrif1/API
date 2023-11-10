from fastapi import APIRouter, Depends, status, HTTPException
from .. import dlschemas, database, models
from sqlalchemy.orm import Session
from ..hash import Hash
from ..dltoken import create_access_token
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=['Auth'])

get_db = database.get_db

@router.post('/login')
def login(login: OAuth2PasswordRequestForm=Depends(), db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == login.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User not found")
    if not Hash.verify(user.password, login.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password, try again")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}