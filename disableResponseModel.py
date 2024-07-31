from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from typing import Union

app = FastAPI()

@app.get("/port", response_model=None)
async def get_teleport(teleport:bool = False) -> Union[Response, dict]:
    if teleport:
        return RedirectResponse(url="http://...")
    return {"message": "hello there!"}
