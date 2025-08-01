import pandas as pd

data_frame = pd.read_csv("nato_phonetic.csv")


data_dictionary = {row.letter: row.code for (index, row) in data_frame.iterrows()}

print(data_dictionary)


name = "Angela"

nato_name = [data_dictionary[letter] for letter in name.upper()]

print(nato_name)