# this variable is global scope
enemies = 1



def increase_enemies():
    # this variable is in local scope
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
