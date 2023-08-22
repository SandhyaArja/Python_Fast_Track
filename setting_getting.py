class Person:
    def __init__(self,name):
        self ._name=name 
    
    @property 
    def name (self):
        print("Getting Value")
        return self._name
        
    @name.setter 
    def name(self,value):
        print("Setting Value")
        self._name=value 
person=Person("Sandhya")
print(person.name)   # Calls the getter method
                      # Calls the setter method
person.name="Shravani"
print(person.name)

