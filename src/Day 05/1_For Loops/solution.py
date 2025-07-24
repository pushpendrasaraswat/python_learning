fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruits.index(fruit))
    print(fruit)


for _ in range(2): # _ is a common convention for a variable that is not used , if we dont want to use the variable
    # and want to repeat the loop for 2 times in this case, this is the way to do it
    print("Hello!")