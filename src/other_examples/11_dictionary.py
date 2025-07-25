to_minutes = 24 * 60
to_seconds = to_minutes * 60
to_Hour = 24
unit_second = "minutes"

def days_to_unit(no_of_days, conversion_unit):
    if conversion_unit == "seconds":
        return f"{no_of_days} days are {no_of_days * to_seconds} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{no_of_days} days are {no_of_days * to_minutes} {conversion_unit}"
    else:
        return f"{no_of_days} days are {no_of_days * to_Hour} {conversion_unit}"


def validate_and_execute():
    try:
        no_of_days = int(days_to_unit_dictionary["days"])
        if no_of_days > 0:
            print(days_to_unit(no_of_days, days_to_unit_dictionary["unit"]) )
        elif no_of_days == 0:
            print("Please enter a non zero number of days.")
        else:
            print("Please enter a positive number of days.")
    except ValueError:
        return "Invalid input. Please enter an integer."


user_input = input("Please enter a number of day and unit seperated by colon: ")
days_and_unit = user_input.split(":")

# we will be creating a dictionary to store the conversion factors
days_to_unit_dictionary ={"days": days_and_unit[0],"unit": days_and_unit[1]}


print(days_to_unit_dictionary)
print(type(days_to_unit_dictionary))

validate_and_execute()