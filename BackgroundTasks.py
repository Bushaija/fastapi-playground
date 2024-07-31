from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_notification(email: str, message=""):
    with open("log.txt", mode = "w") as email_file:
        content = f"notification for {email}:{message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, bg_task: BackgroundTasks):
    bg_task.add_task(write_notification, email, message="some notification")
    return {"message": "notification sent in the background"}
