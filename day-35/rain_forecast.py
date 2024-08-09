from typing import Literal
import requests
from twilio.rest import Client
import os

OWM_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = os.environ.get('OWM_API_KEY')
account_sid = os.environ.get('TWILIO_ACC_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

my_parameters = {
    'lat': 17.40,
    'lon': 78.47,
    'appid': api_key,
    'cnt': 6,
}

response = requests.get(url=OWM_endpoint, params=my_parameters)
response.raise_for_status()

data = response.json()
weather_data_list = data['list']
length_of_list = len(weather_data_list)

# print(data['list'][1]['weather'][0]['id'])

def is_rain() -> None | Literal[True]:
    for hourly_data in weather_data_list:
        condition_code = hourly_data['weather'][0]['id']
        if condition_code < 700:
            return True
    return False

if is_rain() is True:
    # print('Bring an umbrella')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring your umbrella ☔",
        from_='+12562033607',
        to='+91 7416298182',
    )
    print(message.status)
# else:
#     print('The weather is clear')