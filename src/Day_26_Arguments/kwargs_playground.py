

def calculate(n,**kwargs):
    print(type(kwargs))
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(3,add=2, multiply=3))

def different_way(a, *arg, **kw):
    """This function demonstrates the use of *args and **kwargs in a different way.
    a is a positional argument, *arg collects additional positional arguments as a tuple,
    and **kw collects keyword arguments as a dictionary."""

    print(a, arg, kw)

different_way(1, 2, 3, name="John", age=30)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

car1 = Car(make="Ford", model="Mustang")
print(car1.make)
print(car1.model)
print(car1.color)