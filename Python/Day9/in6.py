
class Notification:
    def send(self):
        print("Sending a notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


notification1 = Notification()
notification2 = EmailNotification()
notification3 = SMSNotification()

notifications = [notification1, notification2, notification3]

for notification in notifications:
    notification.send()
