from flight_search import FlightSearch
import datetime as dt
from pprint import pprint

now = dt.datetime.now()
departure_date = (now + dt.timedelta(days=(1))).strftime('%Y-%m-%d')
return_date = (now + dt.timedelta(days=(6*30))).strftime('%Y-%m-%d')


ORIGIN_CITY = 'PAR'
DESTINATION_CITY = 'TYO'
DEPARTURE_DATE = departure_date
RETURN_DATE = return_date
ADULTS = 1
CURRENCY_CODE = 'GBP'

search_flight =  FlightSearch()
data = search_flight.check_flights(
    origin_city= ORIGIN_CITY,
    destination_city= DESTINATION_CITY,
    departure_date= DEPARTURE_DATE,
    return_date= RETURN_DATE,
    adults=ADULTS,
    currency_code=CURRENCY_CODE
)
pprint(data)

