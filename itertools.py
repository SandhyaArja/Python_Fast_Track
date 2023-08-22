#itertools.cycle is a function provided by the itertools module in Python's standard library. 
I#t's used to create an iterator that cycles through the elements of an iterable indefinitely.
import itertools

iterable = [1, 2, 3]
cycle_iter = itertools.cycle(iterable)

for _ in range(10):
    print(next(cycle_iter))

