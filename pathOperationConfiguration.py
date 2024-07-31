from enum import Enum
from typing import Set, Union
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Tags(Enum):
    items = "items"
    users = "users"

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()

@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED
)
async def create_item(item:Item):
    return item


# Tag
@app.post("/items", response_model=Item, tags=["items"])
async def create_item(item:Item):
    return item

# Tag with enum
@app.get("users", tags=[Tags.users])