# Function Factory:

# Using closures to create a function factory that generates custom functions based on different factors.

# python

def exponent_generator(power):
    def exponent(x):
        return x ** power
    return exponent

square = exponent_generator(2)
cube = exponent_generator(3)

print(square(4))  # Output: 16
print(cube(3))    # Output : 27
