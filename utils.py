import os 
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import  Depends
from jose import jwt
from Users import users

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")
load_dotenv() 
secret_key = os.getenv("SECRET_KEY")
def encode_token(payload:dict) -> str:
    token=jwt.encode(payload,secret_key, algorithm="HS256")
    return token

def decode_token(token:Annotated[str,Depends(oauth2_scheme)]) -> dict:
    data= jwt.decode(token,secret_key,algorithms=["HS256"])
    user = users.get(data["username"])
    return user
    