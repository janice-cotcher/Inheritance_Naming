class Wolf:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof!")


husky = Dog("Max", "grey")
husky.bark()