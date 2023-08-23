#itertools.islice is used to create a slice of an iterator
import itertools

numbers = range(10)
sliced_numbers = itertools.islice(numbers, 2, 8)  # Slice from index 2 to 7

for num in sliced_numbers:
    print(num)
