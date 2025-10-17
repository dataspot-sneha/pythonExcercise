                    # Python *args and **kwargs


# By default, a function must be called with the correct number of arguments.
#
# However, sometimes you may not know how many arguments that will be passed into your function.
#
# *args and **kwargs allow functions to accept a unknown number of arguments.

# *args function
#  class type is tuple and position is important

# Arbitrary Arguments - *args
# -------------------------------
# Using *args to accept any number of arguments:

def my_function(*students):
 print("the name of the student is :" + students[1])

my_function("maya","arya","ram")



# if wants to get all tuples print , just avoid + and avoid passing index value

def my_function(*students):
 print("the name of the student is :" ,students)

my_function("maya","arya","ram")



# What is *args?
# The *args parameter allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple containing all the passed arguments:

def my_function(*args):

  print("the type of args :",type(args))
  print("the first position of args :",args[1])
  print("the second position of args :",args[2])
  print("all  of args :",args)

my_function("args1","args2","args3")


# Using *args with Regular Arguments
# You can combine regular parameters with *args.
#
# Regular parameters must come before *args:

def my_function(greetings, *names):
    for name in names:
     print(greetings , name )
my_function("good afternoon","riju","dipu","maya")

# ----------------------------------------------------------------------------------------------------------------------

# Arbitrary Keyword Arguments - **kwargs

# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
#
# This way, the function will receive a dictionary of arguments and can access the items accordingly:

# class type id dictionary and keyword is important

def my_function(**employees):
    print("the name of employee is :",employees["fname"])
my_function(fname="isha",lname="das")

# if we want both first and last name together just use +
def my_function(**employees):
    print("the name of employee is :",employees["fname"]+ employees["lname"] )
my_function(fname="isha",lname="das")

# if we need space in between fname and lname

def my_function(**employees):
    print("the name of employee is :",employees["fname"]+ " " + employees["lname"] )
my_function(fname="isha",lname="das")

# What is **kwargs?
# The **kwargs parameter allows a function to accept any number of keyword arguments.
#
# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

def my_function(**employees):
    print("the type of emloyee",type(employees))
    print("the first position of employees :",employees["fname"])
    print("the second position of employees :",employees["lname"])
    print("print all names of employee:",employees)

my_function(fname="isha",lname="das",age = 34, city = "sweden")

# Using **kwargs with Regular Arguments

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Combining *args and **kwargs
# ------------------------------------
# You can use both *args and **kwargs in the same function.
#
# The order must be:
#
# regular parameters
# *args
# **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("good afternoon","maya","riya",age = 34,location= "kozhikode")
