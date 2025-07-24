import random

#random int
random_integer = random.randint(1, 100)  # Generates a random integer between 1 and 100
print(random_integer)  # Generates a random integer between 1 and 100

#random float
random_float = random.random()  # Generates a random float between 1 and 100
print(random_float)  # Generates a random float between 0 and 1

random_float_range = round(random.uniform(1,10),2) # Generates a random float between 1 and 10
print(random_float_range)  # Generates a random float between 1 and 10

random_heads_tails = random.randint(0, 1)  # Generates a random integer between 0 and 1
if random_heads_tails == 0:
    print("Heads")
else:
    print("Tails")