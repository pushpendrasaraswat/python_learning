"""
try:
expect:
else:
finally:

are the keywords used for error handling in Python.
"""


# FileNotFoundError
try:
    file = open("data.txt")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
    file = open("data.txt","w")  # Create the file if it does not exist1
    file.write("This is a new file created because the original file was not found.")
else:
    for line in file:
        print(line.strip())
finally:
    file.close()
    print("File closed successfully.")


# Key Error  -  key_not_exists
dictionary = {"name": "John", "age": 30}
try:
    print(dictionary["key_not_exists"])
except KeyError as e:
    print(f"Key Error: {e}")


#Index Error
arr = [1, 2, 3]
try:
    print(arr[3])
except IndexError as ie:
    print(f"Index Error: {ie}")


#Type error
try:
    print("1" + 2)
except TypeError as te:
    print(f"Type Error: {te}")
