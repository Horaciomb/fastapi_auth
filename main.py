from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from Utils import encode_token,decode_token
from Users import users
app=FastAPI()



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


