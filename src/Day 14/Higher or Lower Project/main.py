import random

from art import logo, vs
from game_data import data

score = 0


is_choice_consumed = True

def is_correct_choice(first_data, second_data, choicet):
    """Check if the choice is already consumed."""
    if int(first_data["follower_count"]) > int(second_data["follower_count"]) and choicet.lower() == 'a':
        return True
    elif int(first_data["follower_count"]) < int(second_data["follower_count"]) and choicet.lower() == 'b':
        return True
    else:
        return False


while is_choice_consumed:
    print(logo)
    data_a = random.choice(data)

    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")

    print(vs)

    data_b = random.choice(data)
    print(f"Compare B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")

    user_input = input("Who has more followers? Type 'A' or 'B': ")
    choice_response = is_correct_choice(data_a, data_b, user_input)

    is_choice_consumed = choice_response
    if choice_response:
        score += 1
        print(f"You guessed correctly!, your corrent scoAre is {score}")
    else:
        print("You guessed wrong!")
        print(f"Your final score is {score}")
