print(range(1, 10))  # Doesn't do anything

for number in range(1, 10):  # Prints 1 to 9
    print(number)

for number in range(1, 11):  # Prints 1 to 10
    print(number)
print("################")
for number in range(1, 10,2): # Prints 1, 3, 5, 7, 9 (start, stop, step) step is optional and step meaning how many numbers to skip
    print(number)
print("################")
# Gauss challenge
print(sum(range(1, 101)))
total = 0
for number in range(1, 101):
    total += number

print(total)

