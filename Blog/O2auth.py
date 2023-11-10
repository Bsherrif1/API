from fastapi import Depends, HTTPException, status
from fastapi.security import (OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes,)
# import token
from . import dltoken

authenticate_value = 'me'
O2auth_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(data:str = Depends(O2auth_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
        # headers={"WWW-Authenticate": authenticate_value},
    )
    
    return dltoken.verify_token(data, credentials_exception)