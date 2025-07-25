from helper import validate_and_execute, user_input_message
#  from helper import * to import everything from helper.py
# import helper as h alias h to import helper with an alias

#module is a collection of functions and classes that can be used in other Python files single file like helper.py in our example
#package is a collection of modules that can be used in other Python files

user_input = input(user_input_message)
days_and_unit = user_input.split(":")

# we will be creating a dictionary to store the conversion factors
days_to_unit_dictionary ={"days": days_and_unit[0],"unit": days_and_unit[1]}

validate_and_execute(days_to_unit_dictionary)