# You can merge multiple sorted iterables into one sorted sequence using heapq.merge   
import heapq

iterable1 = [1, 4, 7]
iterable2 = [2, 5, 6]
merged = heapq.merge(iterable1, iterable2)

for item in merged:
    print(item)

