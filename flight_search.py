from flight_data import FlightData
import requests

IATA_API = 'https://tequila-api.kiwi.com/locations/query'
IATA_API_KEY = '574Xuyy4DACA-aOnE2wIgDDnJAuPwMq5'

SEARCH_API = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:
    # This class is responsible for structuring the flight data.

    def get_destination_code(self, city_name):


        response = requests.get(url=IATA_API, headers={"apikey": IATA_API_KEY},
                                params={"term": city_name, "location_types": "city"})
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_prices(self, city_name, date_from, date_to, fly_to):
        response = requests.get(url=SEARCH_API, headers={"apikey": IATA_API_KEY},
                                params={"fly_from": city_name,"fly_to": fly_to, "one_for_city": 1, "max_stopovers": 0,
                                        "date_from": date_from, "date_to": date_to, "flight_type": "round",
                                        "nights_in_dst_from": 7, "nights_in_dst_to": 28, "curr": "GBP"
                                        })
        try:
            data = response.json()["data"][0]
        except IndexError:
            print("index exception")
            return None


        flight_data = FlightData(
            price=data["price"],
            city_from=data["route"][0]["cityFrom"],
            airport_from=data["route"][0]["flyFrom"],
            city_to=data["route"][0]["cityTo"],
            airport_to=data["route"][0]["flyTo"],
            travel_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
