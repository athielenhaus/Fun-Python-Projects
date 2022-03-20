# notification manager uses Twilio to send SMS alert when a cheap flight is discovered
import requests
from twilio.rest import Client

# NOTE: account_sid and auth_token must be added to use Twilio
class NotificationManager:
    def __init__(self):
        self.account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    # function to send SMS alert
    def send_message(self, city, cheap_flight):
        nights = cheap_flight["nightsInDest"]
        price = cheap_flight["price"]
        client = Client(self.account_sid, self.auth_token)
        
        # SMS message content
        message = client.messages \
            .create(
            body=f"Cheap flight available to {city}️ for {nights} Nights for EUR {price}",
            from_='+14144090xxx',
            to='+491782028xxx')
        print(message.status)
