import itertools

# Cycle through elements indefinitely
cycle_iter = itertools.cycle(["A", "B", "C"])
for i in range(8):
    print(next(cycle_iter))
