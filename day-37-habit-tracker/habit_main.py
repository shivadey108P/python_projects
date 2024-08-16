import requests
import datetime as dt

USER_NAME = 'shivanarayandey'
TOKEN = 'JDF342FN23JD2J3'
pixela_endpoints = 'https://pixe.la/v1/users'
GRAPH_ID = 'walk10k'

pixela_parameters = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# pixala_response = requests.post(url=pixela_endpoints, json=pixela_parameters)
# print(pixala_response.text)

graph_endpoint = f"{pixela_endpoints}/{USER_NAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Steps Counter',
    'unit': 'steps',
    'type': 'int',
    'color': 'ichou',
    }

headers = {
    'X-USER-TOKEN': TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)


post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today_date = dt.datetime.now()
# date_now = str(today_date.date()).replace('-','')
today_date = dt.datetime(year=2024, month=8, day=10)
date_now = today_date.strftime("%Y%m%d")
# date_format = 
print(date_now)

post_pixel_config = {
    'date': date_now,
    'quantity': '10000'
}

# post_pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(post_pixel_response.text)

put_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date_now}"

put_pixel_config = {
    'quantity': '12600'
}

# put_pixel_response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers) #Update 
# print(put_pixel_response.text)

delete_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date_now}"
delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_pixel_response.text)
