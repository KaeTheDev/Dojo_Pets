from Pet import Pet

# Cat subclass

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)

def sleep(self, name):
    super().sleep(name)
    return self

def eat(self, name):
    super().eat(name)
    return self

def play(self, name):
    super().play(name)
    return self

def noise(self):
    print("GROWL!")
