from fastapi import FastAPI, Form
from typing_extensions import Annotated

app = FastAPI()

@app.get("/login/")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return {"username": username}
