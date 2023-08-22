import itertools

numbers = range(10)
sliced_numbers = itertools.islice(numbers, 2, 7)  # Slice from index 2 to 6

for num in sliced_numbers:
    print(num)
