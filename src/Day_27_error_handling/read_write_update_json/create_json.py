from solution import generate_random_password
import json

password = generate_random_password()
website = input("Enter the website name: ")
email = input("Enter the email address: ")

data = {website:
    {
    "email": email,
    "password": password
    }
}

def create_json_date():
    """Creates a JSON file with the given data."""
    return data

# this is how we write to a json file
# if the file does not exist, it will be created
# if the file exists, it will be overwritten
with open("data.json", "w") as file:
    json.dump(create_json_date(), file, indent=4)
