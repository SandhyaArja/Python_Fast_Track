#Using a Generator Expression:

#Similar to list comprehensions, generator expressions create iterators that produce values on-the-fly.

evens = (x for x in range(10) if x % 2 == 0)
for num in evens:
    print(num)
