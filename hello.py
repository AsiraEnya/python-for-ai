

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

Dog1 = Dog("Buddy", "Golden Retriever")
print(f"My dog's name is {Dog1.name} and he is a {Dog1.breed}.")