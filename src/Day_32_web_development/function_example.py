def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def calculator( calculate_function,n1, n2):
    return calculate_function(n1, n2)


print(calculator(add, 2, 3))
print(calculator(multiply, 2, 3))
print(calculator(divide, 6, 3))
print(calculator(subtract, 7, 3))

def outer_function():
    print("This is the outer function")
    def inner_function():
        print("Hello from the inner function")

    inner_function()

outer_function()

# how to call inner function from outside the outer function
def outer_function():
    print("This is the outer function")
    def inner_function_calling():
        print("Hello from the inner function calling")

    return inner_function_calling

inner_function = outer_function()
inner_function()  # This will call the inner function