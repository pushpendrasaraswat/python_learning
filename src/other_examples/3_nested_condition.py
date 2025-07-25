to_minutes = 24 * 60
to_Seconds = to_minutes * 60
unit_second = "minutes"


def validate_and_execute():
    user_input = input("Enter number of days: ")
    if user_input.isdigit():
        days = int(user_input)
        if days > 0:
            response =  f"{days} days are {days * to_minutes} {unit_second}"
        else:
            response = "Please enter a non zero number of days."
        print(response)
    else:
        print("Invalid input. Please enter an integer.")

validate_and_execute()


