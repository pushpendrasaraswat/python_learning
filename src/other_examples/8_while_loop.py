to_minutes = 24 * 60
to_Seconds = to_minutes * 60
unit_second = "minutes"
user_input = ""

def days_to_unit():
    try:
        no_of_days = int(user_input)
        if no_of_days > 0:
            return f"{no_of_days} days are {no_of_days * to_minutes} {unit_second}"
        elif no_of_days == 0:
            return "Please enter a non zero number of days."
        else:
            return "Please enter a positive number of days."
    except ValueError:
        return "Invalid input. Please enter an integer."

while user_input != "exit":
    user_input = input("Please enter a number: ")
    print(days_to_unit())