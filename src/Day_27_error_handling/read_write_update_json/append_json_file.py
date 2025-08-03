import json
from solution import generate_random_password

password = generate_random_password()
website = input("Enter the website name: ")
email = input("Enter the email address: ")

new_data = {website:
    {
    "email": email,
    "password": password
    }
}

def append_to_json_file():

    try:
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            print(data)
    except FileNotFoundError:
        with open("data.json", "w") as json_file:
            json.dump(new_data, json_file, indent=4)
    else:
        data.update(new_data)

    with open("data.json", "w") as json_file:
        print(data)
        json.dump(data, json_file, indent=4)

append_to_json_file()