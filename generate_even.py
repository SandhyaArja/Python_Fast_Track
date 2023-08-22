def evens_num(s,e):
    for num in range(s,e+1):
        if num %2==0:
            yield num

evens=evens_num(1,10)
for even in evens:
    print(even)
