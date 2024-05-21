class Person:
    def __init__(self, name, age):
        self.name = "Nikola" if name == "Nikola" else f"I am not {name}, I am Nikola"
        self.age = age


person1 = Person("Maxim", 30)
print(person1.name)  # Output: I am not Maxim, I am Nikola

person2 = Person("Nikola", 25)
print(person2.name)  # Output: Nikola
