
# The map() function in Python is used to apply a given function to each item in a sequence (like a list)
# and return a new map object (which can be converted to a list).

# Example:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(lambda x: x * 2, numbers)
print (list(result))

# example of mp function by declaring range here ranges is defined as start = 1 and end = 20 and starting from 1 and
# increamented by 3 eg- 1 **2 = 1 , than 1+3 = 4  that result sqaure 4** = 16

saquares = list(map(lambda x: x ** 2, range(1, 20, 3)))
print(saquares)
cubics = list(map(lambda x: x ** 3, range(1, 20, 3)))
print(cubics)

