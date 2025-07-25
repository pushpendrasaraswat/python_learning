to_minutes = 24*60
to_Seconds = to_minutes*60
unit_second="minutes"

def days_to_unit(no_of_days):
    print(f"{no_of_days} days are {no_of_days * to_minutes} {unit_second}")
    print("All good!")

days_to_unit(20)

days_to_unit(30)
