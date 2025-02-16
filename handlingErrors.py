from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

# custom exception handers
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

items = {"foo": "The foo wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something."}
    )
