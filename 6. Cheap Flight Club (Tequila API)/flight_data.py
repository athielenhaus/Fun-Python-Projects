# flight data includes all the parameters for the types of flights we want to find

from datetime import datetime, timedelta
TIME_RANGE = 60


class FlightData:

    def __init__(self):
        self.home_airport = "FRA"
        self.today = datetime.today()
        self.date_from = self.today.strftime("%d/%m/%Y")
        self.in_six_months = self.today + timedelta(days=TIME_RANGE)
        self.date_to = self.in_six_months.strftime("%d/%m/%Y")
        self.parameters = {"fly_from": self.home_airport,
                      "date_from": self.date_from,
                      "date_to": self.date_to,
                      "nights_in_dst_from": 5,
                      "nights_in_dst_to": 8,
                      "max_fly_duration": 4,
                      "curr": "EUR",
                      "max_stopovers": 0}



