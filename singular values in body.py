from typing import Union, Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

@app.put("/items/{item_id}")
async def update_item(
    item_id:int, item:Item, user:User, importance:Annotated[int, Body()]
):
    results = {
        "item_id":item_id,
        "item":item,
        "user":user,
        "importance":importance
    }
    return results
