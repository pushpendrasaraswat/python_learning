from datetime import datetime

user_input = input("Enter your goal with deadline seperated by colon\n")  # input like learn:19.02.2026

input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

days_left = deadline_date - today_date

print(days_left.seconds)

hours_left = int(days_left.total_seconds() / 3600)

print(f"Your goal is to {goal} and you have {days_left.days} days left to achieve it.")
print(f"Your goal is to {goal} and you have {hours_left} hours left to achieve it.")