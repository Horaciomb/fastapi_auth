from typing import Annotated
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Depends , HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import os 
from dotenv import load_dotenv
# from fastapi.exceptions import HTTPException

from Utils import encode_token,decode_token,authenticate_user, create_access_token,get_current_active_user
from Users import users, fake_users_db
from Models import Token, User

app=FastAPI()
load_dotenv() 
access_token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm,Depends()]):
    user = users.get(form_data.username)
    
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    token = encode_token({"username":user["username"], "email":user["email"]})
    return {"access_token":token}

@app.get("/users/profile")
def profile(my_user:Annotated[dict, Depends(decode_token)]):
    return my_user


@app.post("/token2")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(access_token_expire_minutes))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]