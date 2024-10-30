from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException

app=FastAPI()
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

users={
    "universal":{"username":"universal", "email":"horaciomolinab0@gmail.com", "password":"password"}
}

@app.post("/token")
async def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    user = users.get(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    return user


