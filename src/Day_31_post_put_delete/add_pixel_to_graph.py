import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "user-test"
TOKEN = "A7xP2qW9Bd"
GRAPH_ID = "graph-data"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_value_data ={
    "date": datetime.date.today().strftime("%Y%m%d"),  # Format date as YYYYMMDD
    "quantity" : "25"
}

response = requests.post(url=graph_endpoint,headers=headers, json=graph_value_data)
print(response)
print(response.json())
