import requests
from twilio.rest import Client
import os

LAT = 39.951061
LONG = -75.165619
api_key = os.environ.get("api_key")
exc = 'current,minutely,daily'

parameters = {
    'lat': LAT,
    'lon': LONG,
    'exclude': exc,
    'appid': api_key
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data = weather_data['hourly'][:12]

account_sid = 'AC788f8c0ba31921fbcaa5f7789a4aafc6'
auth_token = os.environ.get('auth')

will_rain = False
for data in weather_data:
    weather_id = data['weather'][0]['id']
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        body="It's gonna rain, bring umbrella",
        from_='+14352721610',
        to=os.environ.get('my_number')
    )
    print(message.status)
