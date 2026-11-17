class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")

person1 = Person("Jehan", 14)
person1.display_info()

# Reflection: It keeps the attribute private and protected from direct modification.
# It allows validation or logic later without changing the rest of the code.
# It follows encapsulation, which makes the class safer and easier to maintain.