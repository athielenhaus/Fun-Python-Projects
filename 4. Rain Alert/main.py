import requests
from twilio.rest import Client

#must insert account_sid and auth_token to connect to Twilio
#account_sid = os.environ['xxxxxxxxxxxxxxx']
#auth_token = os.environ['xxxxxxxxxx']
account_sid = 'xxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxx'

# Provide parameters for my location
parameters = {"appid" : "3f66e11a56035dfce816c38d1f02fcd3",
              "lon" : -8.629105,
              "lat" : 41.157944,
              "exclude" : "current,minutely,daily"}

# Connect to openweather API and get weather data in JSON format
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# define desired time segment based on weather data
time_segment= weather_data["hourly"][:12]
will_rain = False

# determine if it will rain in the defined time segment
for id in time_segment:
    print(id["weather"][0]["id"] )
    if id["weather"][0]["id"] < 700:
        will_rain = True

# if it will rain, connect to Twilio API and send SMS
if will_rain:
    client = Client(account_sid, auth_token)
    
    # define SMS message content, sender and recipient
    message = client.messages \
        .create(
        body="Bring an umbrELLA -ELLA -ELLA EH EH ☂☂☂️",
        from_='+14144090xxx',
        to='+491782028xxx')
    
    #get message status
    print(message.status)
