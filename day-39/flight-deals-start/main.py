#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from flight_data import FlightData
# import time
from notification_manager import NotificationManager

data = DataManager()
search_flight =  FlightSearch()
sheet_data = data.get_data()
# flight_data = FlightData()
# pprint(data.get_data())
notification_manager = NotificationManager()

ORIGIN_CITY = 'LON'
ADULTS = 1
CURRENCY_CODE = 'GBP'

if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = search_flight.get_destination_code(row['city'])
        # pprint(search_flight.get_destination_code(row['city']))
        
    pprint(f"sheet data:\n {sheet_data}")
    
    data.destination_data = sheet_data
    data.update_destination_code()
    
    
    
now = dt.datetime.now()
departure_date = (now + dt.timedelta(days=(1))).strftime('%Y-%m-%d')
return_date = (now + dt.timedelta(days=(6*30))).strftime('%Y-%m-%d')


for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = search_flight.check_flights(
        origin_city= ORIGIN_CITY,
        destination_city=destination['iataCode'],
        departure_date= departure_date,
        return_date=return_date,
        adults= ADULTS,
        currency_code=CURRENCY_CODE
    )
    cheapest_flight = FlightData.find_cheap_flights(flights)
    if cheapest_flight.price != 'N/A' and cheapest_flight.price < destination['lowestPrice']:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                        f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                        f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
    # elif cheapest_flight == 'N/A':
    #     pprint('No Best Price found!')
    else:
        pprint('No Best Price found!')
        pprint(f"{destination['city']}: £{cheapest_flight.price}")
    # time.sleep(2)
