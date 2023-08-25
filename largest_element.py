numbers = [2, 6, 7, 4, 9, 8, 3]

largest_element = numbers[0]  # Assume the first element is the largest

for num in numbers:
    if num > largest_element:
        largest_element = num

print("The largest element in the list is:", largest_element)

