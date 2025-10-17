# Arguments
#
# Information can be passed into functions as arguments.
#
# Arguments are specified after the function name,
# inside the parentheses. You can add as many arguments as you want,
# just separate them with a comma.
#
# The following example has a function with one argument (fname).
# When the function is called,
# we pass along a first name,
# which is used inside the function to print the full name:

# function with one argument

def my_greeing (name):
    print("good morning " + name)

my_greeing("john")
my_greeing("ram")
my_greeing("maya")
my_greeing("arya")

# Parameters vs Arguments

def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument

def my_greeing (name):
    print("Hello", name)
my_greeing("arya")

# Number of Arguments

def my_greeing (fname , lname):
    print("Hello", fname+" "+lname)
my_greeing("john", "tom")

# Number of Arguments only passing one argument instead of two means here fname is pssing no l name ,
# hence error message will get


# def my_greeing (fname , lname):
#     print("Hello", fname+" "+lname)
# my_greeing("john")


# Default Parameter Values
# example: 1

def my_function(name = "friend"):
  print("Hello", name)

my_function("ram")
my_function("john")
my_function()
my_function("maya")

# example :2

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Norway")
my_function("India")
my_function("China")
my_function()

# Keyword Arguments

# You can send arguments with the key = value syntax.

def my_function(animal , name):
  print("I have an", animal)
  print(" my " + animal +"'s name is " + name)

my_function(animal= "dog", name="Jean")

# This way, with keyword arguments, the order of the arguments does not matter.

def my_function(animal , name):
    print("I have an", animal)
    print(" my " + animal +"'s name is " + name)
my_function(name= "john", animal="dog")

# Positional Arguments

# When you call a function with arguments without using keywords, they are called positional arguments.



# Positional arguments must be in the correct order:

def my_function(animal , name):
    print("I have an", animal)
    print(" my " + animal +"'s name is " + name)

my_function( "dog","john")

# The order matters with positional arguments:

def my_function(animal , name):
    print("I have an", animal)
    print(" my " + animal +"'s name is " + name)
my_function("john","dog")


# Mixing Positional and Keyword Arguments
#
# You can mix positional and keyword arguments in a function call.
#
# However, positional arguments must come before keyword arguments:


def my_function(animal , name, age):
  print("i have a " , age , " years old" , animal , "'s name is " , name)

my_function("dog" ,name= "buddy", age = 16)


# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.
#
# To specify positional-only arguments, add , / after the arguments:

def my_function(name, /):
  print("good morning", name)

my_function("john")

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

# With , /, you will get an error if you try to use keyword arguments:

# def my_function(name, /):
#   print("Hello", name)
#
# my_function(name = "Emil")

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, name):
  print("good afternoon", name)

my_function(name = "john")

# Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:

def my_function(name):
  print("good afternoon 2", name)

my_function("john")

# With *,, you will get an error if you try to use positional arguments:

# def my_function(*, name):
#   print("Hello", name)
#
# my_function("Emil")

# Combining Positional-Only and Keyword-Only

# You can combine both argument types in the same function.
#
# Arguments before / are positional-only, and arguments after * are keyword-only:

def my_function (a,b ,/,*,c,d):
 return a+b+c+d
result = my_function(12,20,c = 34, d = 60)
print(result)

# Passing Different Data Types

# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
#
# The data type will be preserved inside the function:

def my_function(vegetables):
  for vegetable in vegetables:
    print(vegetable)

my_vegetables = ["carrot", "beetroot", "tomato"]
my_function(my_vegetables)


# Sending a dictionary as an argument:

def my_function(stsudent):
    print("Name:", stsudent["name"])
    print("Age:", stsudent["age"])

my_student = {"name": "preetha", "age": 25}
my_function(my_student)

# Return Values
# Functions can return values using the return statement:

def my_function(x,y):
    return x + y
result = my_function(1,2)
print(result)

# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more.

def my_function():
    return ["apple","banana","grapes","cherry","leamon"]
friuts = my_function()
# print(friuts [0])
# print(friuts [1])
# print(friuts [2])
# print(friuts [3])
# print(friuts [4])
print(friuts)


# A function that returns a tuple:

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)