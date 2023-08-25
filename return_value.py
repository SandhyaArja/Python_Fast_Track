#Returning a Value
#To return a value from the function use return keyword.

def greet(word):
    msg = "Hello " + word
    return msg

name = input()
greeting = greet(word=name)
print(greeting)
