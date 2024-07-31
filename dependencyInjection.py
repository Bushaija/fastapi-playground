class EmailService:
    def send_email(self, recipient, message):
        print(f"sending email to {recipient}:{message}")

"""
class NotificationManager:
    def __init__(self):
        self.email_service = EmailService()

    def notify(self, recipient, message):
        self.email_service.send_email(recipient, message)

# usage
manager = NotificationManager()
manager.notify("user@gmail.com", "hello, this is a notification")

"""

class NotificationManager:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def notify(self, recipient, message):
        self.email_service.send_email(recipient, message)

# usage with dependency injection
email_service = EmailService()
manager = NotificationManager(email_service)
manager.notify("user@gmail.com", "hello, this is a notification")


