from pyndantics import BaseModel BaseModel

class Item(BaseModel):
    name: str
    description: str|None = None
    price: float
    tax: float|None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "a very nice item.",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

