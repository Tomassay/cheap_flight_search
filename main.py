
from flight_search import FlightSearch
from data_manager import DataManager
import json
import datetime
from notification_manager import NotificationManager
#
dm = DataManager()
flight_data = dm.get_destination_data()

#
# flight_dict = {
#   "prices": [
#     {
#       "city": "Paris",
#       "iataCode": "",
#       "lowestPrice": 54,
#       "id": 2
#     },
#     {
#       "city": "Berlin",
#       "iataCode": "",
#       "lowestPrice": 42,
#       "id": 3
#     },
#     {
#       "city": "Tokyo",
#       "iataCode": "",
#       "lowestPrice": 485,
#       "id": 4
#     },
#     {
#       "city": "Sydney",
#       "iataCode": "",
#       "lowestPrice": 551,
#       "id": 5
#     },
#     {
#       "city": "Istanbul",
#       "iataCode": "",
#       "lowestPrice": 95,
#       "id": 6
#     },
#     {
#       "city": "Kuala Lumpur",
#       "iataCode": "",
#       "lowestPrice": 414,
#       "id": 7
#     },
#     {
#       "city": "New York",
#       "iataCode": "",
#       "lowestPrice": 240,
#       "id": 8
#     },
#     {
#       "city": "San Francisco",
#       "iataCode": "",
#       "lowestPrice": 260,
#       "id": 9
#     },
#     {
#       "city": "Cape Town",
#       "iataCode": "",
#       "lowestPrice": 378,
#       "id": 10
#     }
#   ]
# }

#print(flight_dict['prices'])



if flight_data[0]["iataCode"] == "":
  fs = FlightSearch()
  for row in flight_data:
    row["iataCode"] = fs.get_destination_code(row["city"])
  dm.destination_data = flight_data
  dm.update_destination_code()
#
# print(flight_data)

# FD = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
#       {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
#       {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
#       {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
#       {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
#       {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
#       {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
#       {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
#       {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
six_month_from_tomorrow = tomorrow + datetime.timedelta(days=180)

print(tomorrow)
print(six_month_from_tomorrow)
fs = FlightSearch()
notification_manager = NotificationManager()
for city in flight_data:
      flight = fs.get_prices("LON", tomorrow, six_month_from_tomorrow, city['iataCode'])
      if flight.price < city["lowestPrice"]:
          notification_manager.send_sms(message=f"Fly to {flight.city_to} now on lower price, is for {flight.price}, from {flight.travel_date} to {flight.return_date}")








