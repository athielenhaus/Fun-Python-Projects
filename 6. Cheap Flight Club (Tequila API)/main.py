#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

# instantiate classes to get previously defined flight parameters, api-powered flight search engine and api-powered SMS alert
flight_data = FlightData()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# check spreadsheet for desired destinations
data_manager = DataManager()
cities = data_manager.get_cities()

# get airport codes for each city and add them to spreadsheet
for city in cities:
    search_term = city["destination"]
    city["code"] = flight_search.get_code(search_term)
data_manager.add_codes(cities)


# get the lowest price for each previously established route
for city in cities:
    cheapest_flight = flight_search.get_cheapest_flight(city)
    cheapest_price = cheapest_flight["price"]
    
    # if the lowest price is below previously defined price, send SMS alert
    if cheapest_flight["price"] < city["price"]:
        notification_manager.send_message(city, cheapest_flight)
        
        # check output
        print("great deal available!")
        print(f"{city['destination']} EUR {cheapest_price}")
