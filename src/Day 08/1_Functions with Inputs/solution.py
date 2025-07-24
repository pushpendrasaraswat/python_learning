def greet():
    print("hello")
    print("how you doing ?")
    print("welcome on day 8")

greet()


def greet_user(name):
    print(f"hello {name}")
    print(f"how you doing  {name} ?")
    print(f"{name} welcome on day 8")
print("\n")

greet_user("Michale")
print("============")
greet_user(input("enter your name: "))