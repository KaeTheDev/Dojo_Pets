from Pet import Pet
from Cat import Cat
from Ninja import Ninja



# Creating an instance of the Pet Class
knox = Pet("Knox", "Doberman", "Comedy")
knox.sleep("Knox")
knox.eat("Knox")
knox.play("Knox")
knox.noise()



print("\n==============\n")

# Creating an instance of the Ninja Class

kaethedev = Ninja("Kae", "TheDev", "Dog Biscuits", "Dog Chow", "Dog")
kaethedev.walk()
kaethedev.feed()
kaethedev.bathe()

print("\n==============\n")

# Creating an instance of the Cat Class which is using inheritance

garfield = Cat("Garfield", "Ocelot", "Sleeping")
garfield.sleep("Garfield")
garfield.eat("Garfield")
garfield.play("Garfield")
garfield.noise()


print("\n==============\n")