from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    token: str
class UserOut(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str

class LoginData(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
    
class Token(BaseModel):
    token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None