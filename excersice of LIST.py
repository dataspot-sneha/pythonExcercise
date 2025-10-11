 =================================================================VALUTION=========================================================================

# 1.variable naming rules
# Must start with a letter or underscore (_):
#
# Valid: name, _count, a1
#
# Invalid: 1name, @value
#
# Can contain letters, digits, and underscores (A–Z, a–z, 0–9, _):
#
# Valid: total_marks, age1
#
# Invalid: student-name, marks%
#
# Case-sensitive:
#
# age, Age, and AGE are three different variables.
#
# Cannot use Python keywords (reserved words):
#
#  Invalid: class = "abc", for = 10
# (because class, for are reserved keywords)
#
# No spaces allowed:
#
#  Use underscore: student_name
#
# Invalid: student name

name ="data science"
print(name)

_age = 25
print(_age)

marks1 = 95
print(marks1)

total_marks = 450
print(total_marks)

studentName = "IPSC"
print(studentName)


# 2.Difference between capitalize() and title()

# capitalize() → Makes the first character uppercase and the rest lowercase.
test = "helo world"
print(test.capitalize())

# title() → Makes the first letter of every word uppercase and the rest lowercase.
test = "helo world"
print(test.title())


# 3.Using indexing how to remove last 5 element from the list
# A=[1,2,3,4,5,6,7,8,9,10]

 # using indexing , starts with 0 in first position of element

A = [1,2,3,4,5,6,7,8,9,10]
A = A[:5]
print(A)


# using negative indexing ,start with reverse order with -1

A = [1,2,3,4,5,6,7,8,9,10]
A = A[:-5]
print(A)



# 4. Read your name from user and print it upper case
name = input("Enter your name: ")
print(name.upper())
print(type(name))



# 5.How to check an element is present or not your list
A = [1, 2, 3, 4, 5]

if 3 in A:
    print("3 is present in list of A")


# 6. Create the following list and do the program
# A=[1,2,p,y,k,10,20]
# i. Delete p,y,k,10 in list in one line
# ii. Find the index of k using function

A = [1, 2, "p", "y", "k", 10, 20]
del A[2:6]
print(A)

A = [1, 2, "p", "y", "k", 10, 20]
print(A.index("k"))



# 7. Create the following list and find how much time 10 occurred in list
# A=[2,2,10,3,4,5,1]
# Output: ‘element’ is occurred ‘no of time’ in list A

A = [2, 2, 10, 3, 4, 5, 1]
print("10 is occurred", A.count(10), "time in list A")

A = [2, 2, 10, 3, 4, 5, 1]
B =A.count(5)
print("5 is occured",B ,"time in the list of A")


A = [2, 2, 10, 3, 4, 5, 1, 10, 77, 10]
print("10 is occurred", A.count(10), "time in list A")


A = [2, 2, 10, 3, 4, 5, 1, 10, 77, 10]
print("20 is occurred", A.count(20), "time in list A")

# 8. Read the 3 fruits name print in list
# A=apple
# B=banana
# C=cherry

A ="apple"
B="banana"
C="cherry"
fruits=[A,B,C]
print(fruits)



# 9.Find the reminder of 50 divided 4 and print the output using f string
# A=50
# B=4
# Output : the reminder is ____ when A divided B

X = 50
Y = 4
print(f"The reminder is {X % Y} when X divided Y")

X=50
Y=4
div= X%Y
print(f"the reminder is ",X % Y,"when X divided Y")


# 10.Write a python program input is [1,2,3] and the output will be [1,2,3,1,2,3]
A = [1, 2, 3]
output = A * 2
print(output)

A = [1,2,3]
B = [1,2,3]
print(A+B)

# 11.Write a python program find the second largest element from the following list
# A=[100,50,2,5,7,25,78]

A = [100, 50, 2, 5, 7, 25, 78]
secondlargest = sorted(A)[-2]
print("Second largest element is:", secondlargest)

A = [100, 50, 2, 5, 7, 25, 78]
A.sort()
print(A)
secondlargest =A[-2]
print(secondlargest)


# .12. Write the program to get the following output
# Input = [(2,1),(1,2),(4,4),(3,2),(2,3)(5,4)] and
# output will be [(1,2),(2,1)(2,2)(2,3)(3,2)(4,4,)(5,4)]

pairs = [(2,1),(1,2),(4,4),(3,2),(2,3),(5,4)]
pairs.sort()
print(pairs)



# 13.What is the difference between find() and index() explain using example

# find() → Returns the index value of variable, if element is not found returns r
A= "helo world"
print(A.find("d"))

# index() → returns the index value of variable present, if element is not found return an error message

A = "helo world"
print(A.index("d"))



# 14.Print the following element from the list
# A=[20,kerala,[100,200,300],A,B,C,[15,23,25]]
# i. 23,25
# ii. [100,200,300]
# iii. r
# iv. 15
# v. A,B,C(using negative indexing)

# i. 23, 25
A=[20,"kerala",[100,200,300],A,B,C,[15,23,25]]
print(A[6][1], A[6][2])

# ii. [100,200,300]
A=[20,"kerala",[100,200,300],A,B,C,[15,23,25]]
print(A[2])

# iii. r  (from "kerala")
A=[20,"kerala",[100,200,300],A,B,C,[15,23,25]]
print(A[1][2])

# iv. 15
A=[20,"kerala",[100,200,300],A,B,C,[15,23,25]]
print(A[6][0])

# v. A,B,C (using negative indexing)
A=[20,"kerala",[100,200,300],A,B,C,[15,23,25]]
print(A[-4], A[-3], A[-2])



# 15.Write a program that uses input() twice to get two numbers from the user, multiplies
# the numbers together, and displays the result. If the user enters 2 and 4, then your
# program should print the following text:
# Output: The product of 2 and 4 is 8.0

num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
product = num1 * num2
print(f"The product of {num1} and {num2} is {product}")


# ====================================================================FINISH===================================================================================
