from hangman import HANGMANPICS

user_word = input("Please enter a word: ")

word = user_word.lower()


guessed_letters = []
# Initialize guessed_letters with underscores for each letter in the word
for letter in user_word:
    guessed_letters.append("_")

hangman_index=0

print(HANGMANPICS[hangman_index])

print("".join(guessed_letters))
# Hangman game implementation
# if char it as 2 or more times, we will show all occurrences of the letter

def is_later_in_word(letter, word):
    indices = [i for i, c in enumerate(word) if c == letter]
    for idx in indices:
        guessed_letters[idx] = letter

    found = False
    if letter in word:
        return  True
    else:
        return  False


word_complete = False
while not word_complete:
    input_char = input("Please enter a letter: ")
    result = is_later_in_word(input_char, word)
    if not result :
        hangman_index += 1
        print(HANGMANPICS[hangman_index])


    print("".join(guessed_letters))

    if "_" not in guessed_letters:
        print("You Won!")
        word_complete = True
    else:
        word_complete = False

    if hangman_index == len(HANGMANPICS) - 1:
        print("You lost!")
        word_complete = True

print("The word was " + user_word)
