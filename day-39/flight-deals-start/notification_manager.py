import os
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

SID = os.environ['TWILIO_SID']
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(SID, AUTH_TOKEN)

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_='+12562033607',
            body=message_body,
            to='+918555914966'
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to='whatsapp:+918555914966'
        )
        print(message.sid)