def infinite_counter(start=0):
    while True:
        yield start
        start += 1

# Using the generator
counter = infinite_counter(10)
for n in range(5):
    print(next(counter))

