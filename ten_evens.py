import itertools

evens = itertools.count(start=2, step=2)
first_ten_evens = itertools.islice(evens, 10)

for num in first_ten_evens:
    print(num)

