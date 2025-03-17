from datetime import date

class Notification:
    def __init__(self, notification_id, created_on, content):
        self.notification_id = notification_id
        self.created_on = created_on
        self.content = content

    def send_notification(self):
        # code
        return True

class PostalNotification(Notification):
    def __init__(self, notification_id, created_on, content, address):
        super().__init__(notification_id, created_on, content)
        self.address = address

class EmailNotification(Notification):
    def __init__(self, notification_id, created_on, content, email):
        super().__init__(notification_id, created_on, content)
        self.email = email

