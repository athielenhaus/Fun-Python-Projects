import requests

class DataManager:
    def __init__(self):
        self.header = {"Authorization": "xxxxxxxxxxxxxxxxxxxx"}

    # gets city names from spreadsheet via sheety
    def get_cities(self):
        self.response = requests.get("https://api.sheety.co/xxxxxxxxxxxxxxxxxxxxxxx/flightChecker/data",
                                     headers=self.header)
        self.response.raise_for_status()
        data = self.response.json()
        return data["data"]
    
    # for each city in spreadsheet, adds city code
    def add_codes(self, cities):
        for city in cities:
            parameters = {"data": {"code": city["code"]}}
            response = requests.put(f"https://api.sheety.co/xxxxxxxxxxxxxxxxxxx/flightChecker/data/"
                                    f"{city['id']}",
                                    headers=self.header,
                                    json=parameters)
            response.raise_for_status()
            print(response.text)
