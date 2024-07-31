from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    taxt: Union[float, None] = None
    tags: list[str] = [] # or set[str] = set()
