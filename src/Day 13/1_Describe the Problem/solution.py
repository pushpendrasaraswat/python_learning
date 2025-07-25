def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

def my_function_updated():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function_updated()


# Describe the Problem - Write your answers as comments:
    # 1. Print is not working
# 1. What is the for loop doing?
    # 1. The for loop iterates through numbers from 1 to 19 (inclusive of 1, exclusive of 20).
# 2. When is the function meant to print "You got it"?
    # if i==20:
      #  print("You got it")
# 3. What are your assumptions about the value of i?
    # i will be form 1 to 19, so it will never be equal to 20.
