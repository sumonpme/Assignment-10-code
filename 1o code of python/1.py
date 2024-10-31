# Example 1: Nested lists operations
My_list = [[10,20,30], [40,50], [60,70], [80,90]]
# Accessing a nested element
nested_element=My_list[3][1]
#Modifying a nested element
My_list[1][1]=200
#flattening a nested list
flattened_list = [item for sublist in My_list for item in sublist]
print("Nested_Element:", nested_element)
print("Modified Nested List:" , My_list)
print("Flattened List:" , flattened_list)


