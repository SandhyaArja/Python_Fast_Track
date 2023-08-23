#Chain multiple iterables together
iter1 = [1, 2, 3]
iter2 = [4, 5, 6]
iter3=(7,8,9)
chained_iter = itertools.chain(iter1, iter2,iter3)
print(list(chained_iter))
