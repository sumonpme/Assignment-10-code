#List Comprehension with Conditional Nesting
nested_list = [[1, 2, 3], [8, 7, 15], [9, 10, 20]]
filtered_flattened = [num for sublist in nested_list for num in sublist if num > 10]
print("Filtered Flattened List:", filtered_flattened)  

