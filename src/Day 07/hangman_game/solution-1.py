from hangman import HANGMANPICS

user_word = input("Please enter a word: ")
word = user_word.lower()
user_won = False
guessed_letters = []
hangman_index = 0
placeholder = "_"
for char in user_word:
    placeholder += "_"

print(placeholder)
print(HANGMANPICS[hangman_index])

hangman_index += 1

game_over = False
while not game_over:

     user_guess = input("Guess a letter: ")
     letter_found = False
     display =  ""
     for char in user_word:
         if user_guess == char:
             display += char
             guessed_letters.append(char)
             letter_found = True
         elif char in guessed_letters:
                display += char
         else:
             display += "_"


     print(display)

     if "_" not in display:
         game_over = True
         print("You won!")

     if not letter_found:
        print(HANGMANPICS[hangman_index])
        hangman_index += 1

     if hangman_index == len(HANGMANPICS):
         game_over = True
         print("You Loose!")

