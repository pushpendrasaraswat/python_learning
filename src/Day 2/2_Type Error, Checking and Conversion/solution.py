
# len(12345)
# this code will give an error because len() function is used to find the length of a string, list, tuple, etc. and not for integers.

print(len("Hello World!"))  # This will return the length of the string "Hello World!")
print(len("123456789"))  # This will return the length of the string "123456789")

# to check type of any data
print(type("Hello"))
print(type(123))
print(type(123.45))
print(type(True))

#Type conversion

# You can convert data into different data types using special functions. e.g.
#float()
print(2345.67 + float(123))  # This will convert the integer 123 to a float and add it to 2345.67
#int()
print(int("123")+int("456"))

#str()
print("Hello " + str(123))  # This will convert the integer 123 to a string and concatenate it with "Hello ")
print("number of letters in your name are : "+ str(len(input("What is your name? "))))
