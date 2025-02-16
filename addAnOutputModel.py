from typing import Any, Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

app = FastAPI()

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

