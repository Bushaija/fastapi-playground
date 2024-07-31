from typing import Union
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: Union[str, None] = Field(default=None examples=["a very nice Item"])
    price: float = Field(examples=["35.4"])
    tax: Union[float, None] = Field(default=None, examples=[3.2])

