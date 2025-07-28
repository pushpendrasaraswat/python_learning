letters = ["a", "b", "c", "d", "e","f","g","h"]

print(letters)


print("\nslicing : start from 0 and end before 3rd element\n")
print(letters[:3])
print("\nslicing : start with 2nd element before 4th element\n")
print(letters[2:4])
print("\nslicing : start till end skip every 2nd element\n")
print(letters[::2])

print("\nslicing : start from end till beginning\n")
print(letters[::-1])

piano_tuple = ("do", "re" , "mi", "fa", "so", "la", "ti")
print("\nslicing : also works in case of tuples\n")
print(piano_tuple)
print(piano_tuple[2:5])
print(piano_tuple[::2])
print(piano_tuple[::])
print(piano_tuple[::-1])


