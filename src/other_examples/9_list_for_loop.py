to_minutes = 24 * 60
to_Seconds = to_minutes * 60
unit_second = "minutes"

def days_to_unit():
    try:
        no_of_days = int(no_of_days_element)
        if no_of_days > 0:
            return f"{no_of_days} days are {no_of_days * to_minutes} {unit_second}"
        elif no_of_days == 0:
            return "Please enter a non zero number of days."
        else:
            return "Please enter a positive number of days."
    except ValueError:
        return "Invalid input. Please enter an integer."


user_input = input("Please enter a number: ")

print(type(user_input))
print(type(user_input.split()))
print(user_input + "\n")

for no_of_days_element in user_input.split():# spl;it based on space, if we have specific character we can use that like COMMA
    print(days_to_unit())