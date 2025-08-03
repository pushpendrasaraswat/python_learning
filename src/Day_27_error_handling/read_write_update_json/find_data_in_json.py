import json

website = input("Enter the website name: ")

try:
    with open("data.json", "r") as file:
        data = json.load(file)
        if website in data:
            print(f"email and Password for {website} is: {data[website]["email"]} , {data[website]["password"]}")
        else:
            print(f"No password found for {website}.")
except FileNotFoundError:
    print("No data file found. Please create a data file first.")

