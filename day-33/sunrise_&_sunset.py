import requests
import datetime as dt

MY_LAT = 17.38
MY_LONG = 78.48

time_now = dt.datetime.now()

my_parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response =  requests.get('https://api.sunrise-sunset.org/json', params=my_parameters)
response.raise_for_status

data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)
print(time_now.hour)