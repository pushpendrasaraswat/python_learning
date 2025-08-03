import json


json_file = open("data.json", "r")

data = json.load(json_file)

print(data)
print(type(data))
print(data.get("google"))  # Use get to avoid KeyError if "google" does not exist
print(data["google"])
print(data["google"]["email"])
print(data["google"]["password"])