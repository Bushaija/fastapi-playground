from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user
