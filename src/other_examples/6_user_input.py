to_minutes = 24 * 60
to_Seconds = to_minutes * 60
unit_second = "minutes"

user_input = input("enter number of days: ")
print(user_input)

days = int(user_input)


def days_to_unit(no_of_days):
    print(f"{no_of_days} days are {no_of_days * to_minutes} {unit_second}")
    print("All good!")


def days_to_unit_response(no_of_days):
    return f"{no_of_days} days are {no_of_days * to_minutes} {unit_second}";


days_to_unit(days)

response = days_to_unit_response(days)

print(response)
