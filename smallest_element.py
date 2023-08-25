numbers = [2, 6, 7, 4, 9, 8, 3]

smallest_element = numbers[0]  # Assume the first element is the smallest

for num in numbers:
    if num < smallest_element:
        smallest_element = num

print("The smallest element in the list is:", smallest_element)

