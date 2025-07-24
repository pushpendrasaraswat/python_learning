def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
first_number = float(input("Enter your first number: "))
for symbol in operations:
    print(symbol)
operation = input("Enter your operation: ")
second_number = float(input("Enter your second number: "))

print(operations[operation](first_number, second_number))