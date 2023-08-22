import itertools

counter = itertools.count(start=1, step=2)
for _ in range(5):
    print(next(counter))
