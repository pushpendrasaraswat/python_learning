
# get unspecified number of arguments and add them together
# This is a simple function that takes an unspecified number of arguments and adds them together.
# It uses the *args syntax to accept any number of positional arguments.
# The function iterates through each argument, adds them to a total, and returns the result
def add(*args):
    print(type(args))
    print(args)
    total =0
    for number in args:
        total += number
    return total

print(add(1,2,3,4,5,6,7,8,9,10))
print(add(1,2,3,4))
print(add(1,2,3,4,5,6))
print(add())


