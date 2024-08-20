import requests
from requests.auth import HTTPBasicAuth
import datetime as dt
import os

NUTRITION_API_KEY = os.environ.get('NUTRITION_API_KEY')
APP_ID = os.environ.get('NUTRITION_APP_ID')
NUTRITION_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
SHEETY_API = os.environ.get('SHEETY_API_TOKEN')
SHEETY_PASSWORD = os.environ.get('SHEETY_PASSWORD')
SHEETY_USERNAME = os.environ.get('SHEETY_USERNAME')

AGE = 25
HEIGHT_CM = 162
WEIGHT_KG = 60
GENDER = 'male'
headers = {
    'x-app-id': APP_ID,
    'x-app-key': NUTRITION_API_KEY
}

parameters_exercise = {
    "query" : input('Please enter your exercise routine you performed today:'),
    "age": AGE,
    'height_cm': HEIGHT_CM,
    'weight_kg': WEIGHT_KG,
    'gender': GENDER,
}

today = dt.datetime.now()
today = dt.datetime(year=2024, month=8, day=15)
date_now = today.strftime("%d/%m/%Y")
time_now = today.strftime("%X")



duration_list = []
workout_name = []
calories_list = []

response_calories = requests.post(url=NUTRITION_ENDPOINT, json=parameters_exercise, headers=headers)
workout_data = response_calories.json()['exercises']
length_data = len(workout_data)
for data in workout_data:
    duration_list.append(data['duration_min'])
    workout_name.append(data['name'])
    calories_list.append(data['nf_calories'])
    
print(workout_name)
print(duration_list)
print(calories_list)

for i in range(length_data):
    sheety_params = {
        'workout': {
            'date' : date_now,
            'time' : time_now,
            'exercise' : workout_name[i].title(),
            'duration' : duration_list[i],
            'calories' : calories_list[i]
        }
    }
    basic = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, auth= basic)
    # sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params)
    print(sheety_response.text)