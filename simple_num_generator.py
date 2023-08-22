def num_generator(m):
    i=1 
    while i<= m:
        yield i 
        i+=1 
num=num_generator(7)
for n in num:
    print(n)
