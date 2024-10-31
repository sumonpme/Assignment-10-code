# Converting a list of tuples into a dictionary using a loop
list_tuples = [('x', 1), ('y', 2), ('z', 3)]
conv_dict = {}
for key, value in list_tuples:
    conv_dict[key] = value
print(conv_dict)  
