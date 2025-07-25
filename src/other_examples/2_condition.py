to_minutes = 24 * 60
to_Seconds = to_minutes * 60
unit_second = "minutes"




def days_to_unit(no_of_days):
    if no_of_days < 0:
        return "Please enter a positive number of days."
    elif no_of_days == 0:
        return "Please enter a non zero number of days."
    else:
        return f"{no_of_days} days are {no_of_days * to_minutes} {unit_second}"

def validate_and_execute():
    user_input = input("Enter number of days: ")
    if user_input.isdigit():
        days = int(user_input)
        response = days_to_unit(days)
        print(response)
    else:
        print("Invalid input. Please enter an integer.")

validate_and_execute()


