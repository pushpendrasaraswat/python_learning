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


response = requests.delete(url=graph_endpoint,headers=headers)
print(response)
print(response.json())
