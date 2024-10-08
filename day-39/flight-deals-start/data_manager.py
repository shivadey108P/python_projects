from requests.auth import HTTPBasicAuth
import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
SHEETY_ENDPOINT = 'https://api.sheety.co/4ca841c08117f0eb5fa97ec1339669ac/flightDeals/prices'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self) :
        self.basic = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)
        self.destination_data = {}
        
    def get_data(self):
        self.response =  requests.get(url=SHEETY_ENDPOINT,auth=self.basic)
        self.response.raise_for_status
        self.destination_data = self.response.json()['prices']
        return self.destination_data
    
    def update_destination_code(self):
        for city in self.destination_data:
            new_data_iata = {
                'price':{
                    'iataCode': city['iataCode']
                }
            }
            self.put_response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json= new_data_iata, auth=self.basic)
            pprint(self.put_response.text)