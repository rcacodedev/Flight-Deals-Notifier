from twilio.rest import Client
from config import TWILIO_PHONE, PHONE

class NotificationManager:
    def __init__(self, account_sid, auth_token):
        """
        Initialize the NotificationManager with Twilio credentials.

        :param account_sid: Twilio account SID
        :param auth_token: Twilio authentication token
        """
        self.account_sid = account_sid
        self.auth_token = auth_token

    def send_twilio_message(self, body, to):
        """
        Send a message through Twilio.

        :param body: Message body
        :param to: Destination phone number (default: PHONE)
        :param from_: Source phone number (default: TWILIO_PHONE)
        """
        try:
            client = Client(self.account_sid, self.auth_token)
            message = client.messages.create(
                body = body,
                from_=TWILIO_PHONE,
                to=PHONE
            )
            print(f"Message sent: {message.sid}")
        except Exception as e:
            print(f"Error sending message: {e}")
