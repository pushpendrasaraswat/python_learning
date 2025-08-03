import pandas as pd

data_frame = pd.read_csv("nato_phonetic.csv")


data_dictionary = {row.letter: row.code for (index, row) in data_frame.iterrows()}

print(data_dictionary)

def generate_phonetic():
    """Generates a phonetic code for the given name."""
    # This function is not used in the current implementation but can be used for future enhancements.

    name = input("Enter your name: ")
    try:
        nato_name = [data_dictionary[letter] for letter in name.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_name)

generate_phonetic()