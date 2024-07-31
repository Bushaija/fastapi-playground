from datetime import datetime
from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:32",
    "friends": [1, "2", b"3"]
}

user = User(**external_data) #unpack a dictionary
print(user.name.lower())
