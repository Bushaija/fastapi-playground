from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/teleport')
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="http://...")
