from get_letter_content import read_letter_content

read_file_names_path = "./input/Names/invited_names.txt"

output_file_names_path = "./output/readyToSend/"


template = read_letter_content()

def create_personalized_letters(name):
    file_name = output_file_names_path+"letter_for_"+name+".docx"
    with open(file_name, "w") as output_file:
        personalized_letter = template.replace("[name]", name.strip())
        output_file.write(personalized_letter)


with open(read_file_names_path) as name_file:
    for line in name_file:
        create_personalized_letters(line)





