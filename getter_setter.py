class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting name")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name")
        self._name = value

person = Person("Alice")
print(person.name)  # Calls the getter method
person.name = "Bob"  # Calls the setter method
print(person.name)

