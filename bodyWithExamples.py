from pydantic import BaseModel
from fastapi import FastAPI
from typing import Annotated, Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(
    item_id:int,
    item:Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        )
    ]
):
    resource = {
        "item_id": item_id,
        "item": update_item
    }
    return resource
