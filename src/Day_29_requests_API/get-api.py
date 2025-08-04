import requests

MY_LAT= 51.507351
MY_LONG = -0.127758

response = requests.get("http://api.open-notify.org/iss-now.json")

# respnse code
# 1xx - Informational
# 2xx - Success
# 3xx - Redirection,or you dont have permission
# 4xx - Client Error, or you have made a mistake
# 5xx - Server Error, or the server is down
print(response.status_code)  # 200 means OK, 404 means Not Found, etc.

json_response = response.json()
print(json_response)
latitude = json_response.get("iss_position").get("latitude")
longitude = json_response.get("iss_position").get("longitude")
print(latitude, longitude)

iss_lat = float(latitude)
iss_lon = float(longitude)

print(f"lat and long of the iss position are :{json_response['iss_position']['latitude']}, {json_response['iss_position']['longitude']}")

if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_lon <= MY_LONG + 5:
    print("Look up, the ISS is above you!")

