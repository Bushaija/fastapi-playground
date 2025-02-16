from pydantic import BaseModel, HttpUrl
from typing import Union

# deep nest

class Image(BaseModel):
    name: str
    url: HttpUrl

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    images: Union[list[Image], None] = None # <--

class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[Item] # <--
