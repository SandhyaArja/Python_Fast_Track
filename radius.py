class Circle:
    def __init__(self,radius):
        self._radius =radius 
    @ property 
    def diameter(self):
        return self._radius*2 

    @ property 
    def circum(self):
        return 3.14159*self.diameter 
circle = Circle(5)
print(circle.diameter)
print(circle.circum)
