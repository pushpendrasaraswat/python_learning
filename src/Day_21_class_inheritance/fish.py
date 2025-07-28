from animal import Animal


class Fish(Animal):

    def __init__(self,name):
        super().__init__(name)


    def breathe(self):
        super().breathe()
        print(f"{self.name} is breathing underwater")

    def swim(self):
        print(f"{self.name} is swimming")