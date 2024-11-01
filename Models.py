from pydantic import BaseModel


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