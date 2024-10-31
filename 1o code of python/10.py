# Tuple Comprehension using Generator Expression
basic_numbers = [1, 2, 3, 4, 5, 6, 7, 8,]
# Using a generator expression to create a tuple of squares of even numbers
even_squares_tuple = tuple(num ** 2 for num in basic_numbers if num % 2 == 0)
print("Tuple of Even Squares:", even_squares_tuple)  

