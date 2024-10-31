# Set comprehension with condition
My_set = {5, 10, 15, 20, 25, 30}
square_numbers = {x**2 for x in My_set if x % 2 == 0}
print(square_numbers)  

