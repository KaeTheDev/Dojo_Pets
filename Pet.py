class Pet:
    def __init__(self, name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    def sleep(self, name):
        energy = 0

        energy = energy + 25
        print(f"{self.name} gained 25 in energy")

    def eat(self, name):
        energy = 0
        health = 0
        
        energy = energy + 5
        health = health + 10

        print(f"{self.name} gained 5 in energy and 10 in health")

    def play(self, name):
        health = 0

        print(f"{self.name} gained 5 in health")

    def noise(self):
        print("WOOF!")

