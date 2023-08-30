class One:
    def display(self):
        print("This is Parent class")

class Two(One):
     def display(self):
        print("This is child1 class")
    
class Three(Two):
      def display(self):
        print("This is child2 class")

d=Two()
d.display()
