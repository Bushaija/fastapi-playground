from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from typing import Union, Any

app = FastAPI()

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Union[Response, dict]:
    if teleport:
        return RedirectResponse(url="http://...")
    return {"message": "here's your interdimensional portal."}
