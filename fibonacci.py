def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator
fibonacci = fibonacci_generator()
for i in range(10):
    print(next(fibonacci))
# will print 1st 10 fibonacci numbers
