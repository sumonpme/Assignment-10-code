# Dictionary merging with comprehension
M1 = {'a': 1, 'b': 2 , 'c':3}
M2 = {'b': 4, 'c': 5, 'd': 6}
merged_dict = {key: (M1.get(key, 0) + M2.get(key, 0)) for key in M1.keys() | M2.keys()}
print(merged_dict)  

