import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "user-test"
TOKEN = "A7xP2qW9Bd"


user_params = {
    "token" : "A7xP2qW9Bd",
    "username" : "user-test",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# Sending a POST request to create a new user on Pixela and commenting the response
# response = requests.post(url=pixela_endpoint, json=user_params)
#print(response)
#print(response.json())


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph-data",
    "name":"Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",

}

headers = {
    "X-USER-TOKEN":TOKEN
}

response = requests.post(graph_endpoint,headers=headers, json=graph_config)
print(response)
print(response.json())