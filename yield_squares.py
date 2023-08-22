def square_generato(limit):
    for num in range(1,limit+1):
        yield num**2

limit =10 
squares = square_generato(limit)
for square in squares:
    print(square)
