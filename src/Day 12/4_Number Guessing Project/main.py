from art import logo
import random
print(logo)

number_to_guess= random.randint(1,100)
print(number_to_guess)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


is_number_guessed = False
def is_number_correct(guessed_number):
    return guessed_number == number_to_guess

while not is_number_guessed :
    guessed_number = int(input("Guess a number between 1 and 100: "))

    is_number_guessed = is_number_correct(guessed_number)

    if is_number_guessed:
        print(f"You guessed the number in {guessed_number}.")
        break
    elif guessed_number > number_to_guess:
        print(f"Guessed number is higher then the Number.")
    else :
        print(f"Guessed number is lower then the Number.")
