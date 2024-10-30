from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from utils import encode_token,decode_token
app=FastAPI()


users={
    "universal":{"username":"universal", "email":"horaciomolinab0@gmail.com", "password":"password"}
}



@app.post("/token")
async def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    user = users.get(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    
    token = encode_token({"username":user["username"], "email":user["email"]})
    return {"access_token":token}

@app.get("/users/profile")
def profile(my_user:Annotated[dict, Depends(decode_token)]):
    return my_user


