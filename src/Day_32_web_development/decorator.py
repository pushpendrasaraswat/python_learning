import time


# python decorator function, decorstor function is a function which takes another function
# as an argument and extends the behavior of the original function without explicitly modifying it.
# In this example, we will create a decorator function that adds a delay before executing the original function.

def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@decorator_function
def say_hello():
   print("Hello, World!")




decorated_function = decorator_function(say_hello)
decorated_function()