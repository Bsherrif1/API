from passlib.context import CryptContext

pwd_con = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password:str):
        hashedpass = pwd_con.hash(password)
        return hashedpass
    
    def verify(hashed_pass, plain_pass):
        return pwd_con.verify(plain_pass, hashed_pass)