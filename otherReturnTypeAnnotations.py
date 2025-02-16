from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=...")
    return JSONResponse(content={"message":"Here's your interdimensional portal."})

'''
    response
        - JSONResponse
        - RedirectResponse
'''

