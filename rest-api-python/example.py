import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    json_data = response.json()
    for data in json_data:
        print(data.get("id"))
        print( data["name"], data["email"])


arr = [{"a"},{"b"},{"c"}]

for item in arr:
    if item == {"a"}:
        arr.remove(item)

print(arr)
