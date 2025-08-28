# Base class representing a generic animal in a zoo
class ZooAnimal:
    # Constructor to initialize common attributes
    def __init__(self, name, species, age):
        self.name = name            # Name of the animal (e.g., "Leo")
        self.species = species      # Species of the animal (e.g., "Lion")
        self.age = age              # Age of the animal in years
        self.is_awake = True        # Tracks if the animal is awake or asleep

    # Method to toggle awake/asleep state
    def toggle_awake(self):
        self.is_awake = not self.is_awake
        status = "awake" if self.is_awake else "asleep"
        print(f" {self.name} the {self.species} is now {status}.")

    # Abstract method for movement (must be implemented by subclasses)
    def move(self):
        raise NotImplementedError("Subclass must implement move()")

    # Abstract method for making a sound (must be implemented by subclasses)
    def make_sound(self):
        raise NotImplementedError("Subclass must implement make_sound()")

    # Method to display animal details
    def info(self):
        if not self.is_awake:
            print(f" {self.name} the {self.species} is asleep and cannot display info.")
            return
        print(f" {self.name} the {self.species}")
        print(f"   Age: {self.age} years")


# Child class for a terrestrial animal (e.g., Lion)
class Lion(ZooAnimal):
    # Constructor with additional attribute
    def __init__(self, name, age, mane_color):
        super().__init__(name, "Lion", age)
        self.mane_color = mane_color  # Unique attribute for lions

    # Implementation of move method
    def move(self):
        if not self.is_awake:
            print(f" {self.name} the Lion is asleep and cannot move.")
            return
        print(f" {self.name} the Lion is prowling with its {self.mane_color} mane!")

    # Implementation of make_sound method
    def make_sound(self):
        if not self.is_awake:
            print(f" {self.name} the Lion is asleep and cannot roar.")
            return
        print(f" {self.name} the Lion roars loudly: ROAR!")


# Child class for an avian animal (e.g., Parrot)
class Parrot(ZooAnimal):
    # Constructor with additional attribute
    def __init__(self, name, age, feather_color):
        super().__init__(name, "Parrot", age)
        self.feather_color = feather_color  # Unique attribute for parrots

    # Implementation of move method
    def move(self):
        if not self.is_awake:
            print(f" {self.name} the Parrot is asleep and cannot fly.")
            return
        print(f" {self.name} the Parrot is flying with {self.feather_color} feathers!")

    # Implementation of make_sound method
    def make_sound(self):
        if not self.is_awake:
            print(f" {self.name} the Parrot is asleep and cannot squawk.")
            return
        print(f" {self.name} the Parrot squawks: SQUAWK!")


# Child class for an aquatic animal (e.g., Dolphin)
class Dolphin(ZooAnimal):
    # Constructor with additional attribute
    def __init__(self, name, age, fin_size):
        super().__init__(name, "Dolphin", age)
        self.fin_size = fin_size  # Unique attribute for dolphins

    # Implementation of move method
    def move(self):
        if not self.is_awake:
            print(f" {self.name} the Dolphin is asleep and cannot swim.")
            return
        print(f" {self.name} the Dolphin is leaping with a {self.fin_size} fin!")

    # Implementation of make_sound method
    def make_sound(self):
        if not self.is_awake:
            print(f" {self.name} the Dolphin is asleep and cannot click.")
            return
        print(f" {self.name} the Dolphin clicks: CLICK-CLICK!")


# Creating a list of zoo animals (polymorphism in action)
zoo_animals = [
    Lion("Leo", 5, "golden"),
    Parrot("Polly", 2, "red"),
    Dolphin("Flipper", 3, "large")
]

# Demonstrating polymorphism by iterating over animals
print("=== Zoo Animal Behaviors ===")
for animal in zoo_animals:
    animal.info()           # Display animal details
    animal.move()           # Call move method (different for each subclass)
    animal.make_sound()     # Call make_sound method (different for each subclass)
    print()                 # Empty line for readability

# Demonstrate awake/asleep state
print("=== Testing Sleep State ===")
zoo_animals[0].toggle_awake()  # Put Leo to sleep
zoo_animals[0].info()          # Should show asleep message
zoo_animals[0].move()          # Should show asleep message
zoo_animals[0].make_sound()    # Should show asleep message
zoo_animals[0].toggle_awake()  # Wake Leo up
zoo_animals[0].move()          # Should now work