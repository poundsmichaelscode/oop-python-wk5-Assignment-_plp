
### ✅ Activity 1: Class with Constructor, Inheritance & Encapsulation
## We'll create a **Superhero** base class and a FlyingHero subclass.

# Base class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.__level = level  # encapsulated/private attribute

    def show_identity(self):
        return f"I am {self.name}, and my power is {self.power}!"

    def get_level(self):
        return self.__level

    def level_up(self):
        self.__level += 1
        print(f"{self.name} leveled up to {self.__level}!")

# Subclass with Inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

# Create instances
hero1 = Superhero("ShadowStrike", "Invisibility", 5)
hero2 = FlyingHero("SkyBlazer", "Flight", 8, 300)

# Interact with them
print(hero1.show_identity())
hero1.level_up()
print()

print(hero2.show_identity())
hero2.fly()
hero2.level_up()


### Activity 2: Polymorphism Challenge
##We'll create different types of vehicles that all have a `.move()` method but behave differently!


class Vehicle:
    def move(self):
        print("This vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the water 🚤")

# Polymorphism in action!
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
