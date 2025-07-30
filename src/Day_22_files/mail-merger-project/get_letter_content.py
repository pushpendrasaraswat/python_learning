read_file_letter_path = "./input/Letters/starting_letter.txt"

def read_letter_content():
    with open(read_file_letter_path) as letter_file:
        return letter_file.read()
