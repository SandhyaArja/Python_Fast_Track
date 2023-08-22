import itertools

iterable1 = [1, 2, 3]
iterable2 = ('a', 'b', 'c')
iterable3="ABC"
chained_iter = itertools.chain(iterable1, iterable2,iterable3)

for item in chained_iter:
    print(item)
