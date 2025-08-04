import requests
import datetime

MY_LAT= 51.507351
MY_LONG = -0.127758

url = "https://api.sunrise-sunset.org/json"

parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}  # formatted=0 gives time in UTC, 1 gives local time
response = requests.get(url, params=parameters)


data = response.json()
print(data)
results = data.get("results")  # This will give you the results dictionary
sunrise = results.get("sunrise")
sunset = results.get("sunset")
print(f" sunrise and sunset are : {sunrise} and {sunset} in UTC time")


# get hour for sunrise and sunset time
# format is 2025-08-03T00:41:47+00:00 and 2025-08-03T13:39:46+00:00  split it on T and : get hour like 13

sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
sunset_hour = int(sunset.split("T")[1].split(":")[0])

print(f"sunrise and sunset hour are : {sunrise_hour} and {sunset_hour}")


time_now = datetime.datetime.now().hour

print(f"current time is {time_now}")


if sunset_hour <= time_now:
    print("Look up")


