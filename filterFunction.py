# he filter() function is used to select items from a sequence (like a list) that meet a specific condition.

# It returns only those elements which the condition

# the filter returns the result in form of list

# To see the actual values, you need to convert it to a list using list()

# example

# from functools import filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda num: num % 2 == 0, numbers)
print(list(even))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = filter(lambda num: num ** 2, numbers)
print(list(square))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(map(lambda x : x **2 , numbers))
print(even_squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, numbers)))
print(even_squares)


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Filter even numbers
# Step 2: Square them
# Step 3: Reduce to sum the squares


even_squares = list(map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, numbers)))
print("Even squares:", even_squares)
sum_of_even_squares = reduce(lambda x, y: x + y, even_squares)
print("Sum of even squares:", sum_of_even_squares)
