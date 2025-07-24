def format_name(f_name, l_name):
    """ This is doc string which will be used to describe the function.when you hover the mouse on the function calling place.
    Take a first and last name and format it to return the
    title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("FiRst", "LASt")

length = len(formatted_name)

print(formatted_name)
print(length)

