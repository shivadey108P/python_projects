import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_SECRET_KEY = os.environ["AMADEUS_SECRET"]
AMADEUS_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
FLIGHT_OFFER_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
IATA_ENDPOINT = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self) -> None:
        self._api_key = AMADEUS_API_KEY
        self._secret_key = AMADEUS_SECRET_KEY
        self._token = self._get_new_toke()
    
    def get_destination_code(self, city_name):
        header = {
            'Authorization': f'Bearer {self._token}'
        }
        query = {
            'keyword': city_name,
            # 'max': 2,
            'include': 'AIRPORTS',
            
        }
        response = requests.get(url=IATA_ENDPOINT, params= query, headers= header)
        response.raise_for_status
        code = response.json()['data'][0]['iataCode']
        return code
        
    
    def _get_new_toke(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        body ={
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._secret_key
        }
        response_amadeus = requests.post(url=AMADEUS_ENDPOINT, headers=header, data=body)
        
        pprint(response_amadeus.json()['access_token'])
        return response_amadeus.json()['access_token']
    
    def check_flights(self, origin_city, destination_city, departure_date, return_date, adults, currency_code):
        header = {
            'Authorization': f'Bearer {self._token}'
        }
        query = {
            'originLocationCode': origin_city,
            'destinationLocationCode': destination_city,
            'departureDate': departure_date,
            'returnDate': return_date,
            'adults': adults,
            'nonStop': 'true',
            "currencyCode": currency_code,
            "max": "10",
        }
        
        response = requests.get(url=FLIGHT_OFFER_ENDPOINT, headers=header, params=query)
        response.raise_for_status
        data = response.json()
        return data
        