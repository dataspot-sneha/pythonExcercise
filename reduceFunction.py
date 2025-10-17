# The reduce() function in Python is used to apply a function to all the items in a sequence,
# one by one, to reduce them to a single value.
#
# It comes from the functools module.

# the error happens because the reduce() function always passes two arguments to the function you give it — not one.

# example
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x,y: x + y, numbers)
print (result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x,y: x*y, numbers)
print (product)

