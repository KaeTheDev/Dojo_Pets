from Pet import Pet

class Ninja:

    # class variables go here

    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Knox", "Doberman", "Comedy")

    def walk(self):
        print(f"Kae took {self.pet.name} for a walk.")
        self.pet.play("Knox")

    def feed(self):
        print(f"Kae fed {self.pet.name} a dog biscuit.")
        self.pet.eat("Knox")

    def bathe(self):
        print(f"Kae bathed {self.pet.name}.")
        self.pet.noise()
