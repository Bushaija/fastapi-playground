'''
    other data types
        - UUID: universal unique identifier.
                used as an ID in databases and system.

        - datetime.datetime: timestamp [date+time]
        - datetime.date [date only]
        - datetime.time [time only]
        - datetime.delta [seconds in float]
        - frozenset ?
        - bytes
        - decimal
'''
from fastapi import FastAPI, Body
from datetime import datetime, timedelta, time
from uuid import UUID
from typing import Annotated, Union

app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[Union[time, None], Body()] = None
):
    start_process = start_datetime + process_bar
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_bar,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
