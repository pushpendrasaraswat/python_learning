programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}


print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

#This is how you can add new items to an existing dictionary:
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

print ("\nkey and value pairs in the dictionary:")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

print("creating a new dictionary")
new_dictionary = {}

print(new_dictionary)

new_dictionary[1]="a"
new_dictionary[2]="b"
new_dictionary[3]="c"
new_dictionary[1]="a"
new_dictionary[1]="d"

print(new_dictionary)