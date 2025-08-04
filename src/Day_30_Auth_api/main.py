import requests
import os

api_key = os.getenv("API_KEY")

LAT = lat = 18.520430
LONG = 73.856743

parameter = {
    "lat": LAT,
    "lon": LONG,
    "cnt":4,
    "appid": api_key,
}

URL = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(URL, parameter)
response.raise_for_status()

json_response = response.json()

will_rain = False
for weather in json_response['list']:
    for row in weather['weather']:
        if int(row['id']) < 700:
            will_rain = True


if will_rain:
    print("Bring an umbrella")


