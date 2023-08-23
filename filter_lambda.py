# Filtering Elements:

# the filter() function with a lambda function and an iterator to filter elements from a sequence.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered=filter(lambda x:x%2==0,data)

for even_number in filtered:
    print(even_number)

