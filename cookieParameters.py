# import
from fastapi import FastAPI, Cookie

from typing import Annotated

# usage
app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}

'''
    a cookie is small piece of data stored on user's computer by a web browser.
    contains information about the user, such as:
        - login status
        - preferences
        - tracking info across sessions and websites

    cookie data
        - name, value, domain, path, expiration date, secure flag(optional)
        - HttpOnly flag (optional)
        - SameSite attribute (optional)
'''


