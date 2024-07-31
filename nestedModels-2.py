from pydantic import BaseModel
from typing import Union, HttpUrl


# basic

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    image: Union[Image, None] = None

# url-type
class Image(BaseModel):
    url: HttpUrl
    name: str

# attributes with lists

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    images: Union[list[Image], None] = None


# body
{
    "name": "foo",
    "description": "the pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock","metal","bar"],
    "image": {
        "url": "http://example.com/bar.jpg",
        "name": "The foo live"
    }
}
