#Function Arguments
#A function can have more than one argument.



#Keyword Arguments
#Passing values by their names.


def greet(arg_1, arg_2):
  print(arg_1 + " " + arg_2)

greeting = input()
name = input()
greet(arg_1=greeting,arg_2=name)
