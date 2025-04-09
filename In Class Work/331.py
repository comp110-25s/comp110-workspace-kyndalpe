class Pet:

    name: str
    breed: str

    def __init__(self, pet_name: str, pet_breed: str):
        self.name = pet_name
        self.breed = pet_breed

    def speak(self):
        if self.breed == "dog":
            print("Woof!")
        else:
            print("*silence*")


a1: Pet = Pet("Fido", "dog")
a2: Pet = Pet("Fluffy", "cat")
