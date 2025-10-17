
# A function is a block of code which only runs when it is called.
#
# A function can return data as a result.
#
# A function helps avoiding code repetition.

# Creating a Function
# In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def greet():
    print("Hello world")
greet()

# repeatedly  calling function method

def greet():
    print("Hello world repeating")
greet()
greet()
greet()
greet()

# method of calling function

def  number1_to_number2(number):
    return (number * 2) +100

print(number1_to_number2(100))
print(number1_to_number2(900))
print(number1_to_number2(700))

# negative number

def value1_to_value2(value):
    return (value - 200)* 400

print(value1_to_value2(10))
print(value1_to_value2(20))
print(value1_to_value2(30))

#
# Return Values

# Functions can send data back to the code that called them using the return statement.
#
# When a function reaches a return statement, it stops executing and sends the result back:
# using a new variable (message)

def greeting():
    return "Hello world from python function"
message = greeting()
print(message)

# without using a new variable

def greet():
    return "Hello world from python function without using a new variable"
print(greet())


# The pass Statement
# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

def greet():
    pass
