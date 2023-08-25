#Function With Arguments
#We can pass values to a function using an Argument.



def greet(word):
    msg = "Hello " + word
    print(msg)

name = input()
greet(word=name)
