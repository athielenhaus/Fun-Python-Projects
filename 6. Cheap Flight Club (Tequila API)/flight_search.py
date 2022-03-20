import requests
from flight_data import FlightData

# NOTE: must add apikey to use tequila API
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {"apikey": "xxxxxxxxxxxxxxxxxxxxxxx"}

    # uses the API to check for cheapest flights to destinations indicated in spreadsheet while using parameters defined in flight_data.py 
    def get_cheapest_flight(self, city):
        # for each route, get flights
        flight = FlightData()
        flight.parameters["fly_to"] = city["code"]
        response = requests.get("https://tequila-api.kiwi.com/v2/search?",
                                params=flight.parameters,
                                headers=self.headers)
        response.raise_for_status()
        data = response.json()
        flights = data["data"]
        return self.check_lowest_price(flights)

    def check_lowest_price(self, flights):
        cheapest_flight = ""
        lowest_price = 10000
        for flight in flights:
            price = flight["price"]
            if price < lowest_price:
                cheapest_flight = flight
            return cheapest_flight

    # gets the city airport code via the API
    def get_code(self, term):
        parameters = {"term": term}
        response = requests.get("https://tequila-api.kiwi.com/locations/query?",
                                params=parameters,
                                headers=self.headers)
        response.raise_for_status()
        data = response.json()
        city_code = data["locations"][0]["code"]
        return city_code
