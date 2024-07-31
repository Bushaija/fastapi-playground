from pydantic import BaseModel, Field
from typing import Union
from fastapi import FastAPI

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None,
        description="The description of an item",
        max_length=300
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than 0"
    )
    tax: Union[float, None] = None

app = FastAPI()

@app.put("item/{item_id}")
async def update_item(item_id:int, item:Item):
    results = {"item_id": item_id, "item": item}
    return results
