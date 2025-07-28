def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator(a, b, function):
    return function(a, b)


function_add = add
function_subtract = subtract
function_multiply = multiply
function_divide = divide

result_add = calculator(2, 3, function_add)
result_subtract = calculator(2, 3, function_subtract)
result_multiply = calculator(2, 3, function_multiply)
result_divide = calculator(2, 3, function_divide)

print(f"Result of {function_add.__name__}: {result_add}")
print(f"Result of {function_subtract.__name__}: {result_subtract}")
print(f"Result of {function_multiply.__name__}: {result_multiply}")
print(f"Result of {function_divide.__name__}: {result_divide}")
