import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "user-test"
TOKEN = "A7xP2qW9Bd"
GRAPH_ID = "graph-data"

date = datetime.date.today().strftime("%Y%m%d")

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_value_data ={
    "quantity" : "35"
}

response = requests.put(url=graph_endpoint,headers=headers, json=graph_value_data)
print(response)
print(response.json())
