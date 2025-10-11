
  # =======================# QUESTIONS OF IF ELIF AND ELSE=======================================================

# 1. Write a program a number is positive or negative and (odd and even)

num = int(input("enter a number"))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 2. Eligible for vote or note

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#
# 3.Read float value from user and check in decimal part have any number print that
# o.w print integer value of that number

number = float(input("Enter a number: "))

if number == int(number):
    print("Integer value:", int(number))
else:
    print("The number has a decimal part.")


#
# Write a program to check whether a number entered by user is multiple of 7 or
# not

num = int(input("Enter a number: "))
if num % 7 == 0:
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")

# 5. Write a programme to display ‘hello’ if a number entered by user is multiple of
# five otherwise print “bye”

num = int(input("Enter a number: "))
if num % 5 == 0:
    print("hello.")
else:
    print("bye.")

# 6. Write a program to accept a number from 1 to 7 and display the name of the day
# like 1 for Sunday ,2 for Monday and so on

day = int(input("Enter a number: "))
if day == 1:
    print("The day is Sunday.")
if day == 2:
    print("The day is Monday.")
if day == 3:
    print("The day is Tuesday.")
if day == 4:
    print("The day is Wednesday.")
if day == 5:
    print("The day is Thursday.")
if day == 6:
    print("The day is Friday.")
if day == 7:
    print("The day is Saturday.")
if day > 7 or day < 1:
    print("Invalid number.")

# Write a program to check whether a number entered is three digit number or
# not


num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("The number is a three-digit number.")
else:
    print("The number is not a three-digit number.")

# 8. Write a program to find the lowest number out of 2 number excepted from user

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 < number2:
    print(f"The lowest number is {number1}")
elif number2 < number1:
    print(f"The lowest number is {number2}")
else:
    print("Both numbers are equal")

# 9.Write a program to find the largest number out of two numbers excepted from
# user

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > number2:
    print(f"The largest number is {number1}")
elif number2 > number1:
    print(f"The largest number is {number2}")
else:
    print("Both numbers are equal")



# 10. Write a program to whether a number is divisible by 2 and 3

number = int(input("Enter a number: "))

if number % 2 == 0 and number % 3 == 0:
    print(f"The number {number} is divisible by both 2 and 3.")
elif number % 2 == 0:
    print(f"The number {number} is divisible by 2 but not by 3.")
elif number % 3 == 0:
    print(f"The number {number} is divisible by 3 but not by 2.")
else:
    print(f"The number {number} is not divisible by 2 or 3.")

# 11. Accept the age of 4 people and display the youngest one

age = int(input("Enter your age: "))

a = int(input("Enter age 1: "))
b = int(input("Enter age 2: "))
c = int(input("Enter age 3: "))
d = int(input("Enter age 4: "))

if a < b and a < c and a < d:
    print("Youngest age is:", a)
elif b < a and b < c and b < d:
    print("Youngest age is:", b)
elif c < a and c < b and c < d:
    print("Youngest age is:", c)
else:
    print("Youngest age is:", d)


# 12. Accept age of 4 people and display the oldest one


age = int(input("Enter your age: "))

a = int(input("Enter age 1: "))
b = int(input("Enter age 2: "))
c = int(input("Enter age 3: "))
d = int(input("Enter age 4: "))

if a > b and a > c and a > d:
    print("oldest age is:", a)
if b > a and b > c and b > d:
    print("oldest age is:", b)
if c > a and c > b and c > d:
    print("oldest age is:", c)
else:
    print("oldest age is:", d)

# 13. Write a program to check a character is vowel or not


string = input("Enter a character: ")

if string not in ("a", "e", "i", "o","u"):
    print("enter letter is not vowel")
else:
    print("enter letter is vowel")

# 14. Accept three sides of a triangle and check whether it is equilateral ,isosceles or
# scalene triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# 16. Check if a value 200 exists in a dictionary
# sampleDict = {&#39;a&#39;: 100, &#39;b&#39;: 200, &#39;c&#39;: 300}

sampleDict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sampleDict.values():
    print("Yes, 200 exists")
else:
    print("No, 200 does not exist")


# 18. write a program to check whether last digit of a number (entered by user) is
# divisible by 3 or not.

num = int(input("Enter a number: "))
last_digit = num % 10
# to get second last digit (num // 10)%10, to get third last digit (num // 100)%10, to get fourth last digit (num // 1000)%10
if last_digit % 3 == 0:
    print("Yes, the last digit is divisible by 3")
else:
    print("No, the last digit is not divisible by 3")

# 19. Write a program to check given number is 2 digit or 3 digit or 4 digit

num = int(input("Enter a number: "))

if 10 <= abs(num) <= 99 or 100 <= abs(num) <=999  or 1000 <= abs(num) <=9999:
    print("The number is a two digit ,three-digit , four digit number.")
else:
    print("The number is not a two digit ,three-digit , four digit number.")


# 21. using nested IF ELSE and write a program based on age. Their age 18 and above
# (print adult), between 13 and 17( teenager) or 13 bellow is print as child.
#
# (user input age must be 18 and below)


age = int(input("Enter your age: "))

# Check age using nested if-else
if age >= 18:
    print("Adult")
else:
    if age >= 13:
        print("Teenager")
    else:
        print("Child")

# 21. using nested IF ELSE and write a program based on age. Their age 18 and above
# (print adult), between 13 and 17( teenager) or 13 bellow is print as child.
#
# (user input age must be 18 and below) other way

userAge = int(input("Enter your age: "))

if userAge >= 18:
    print("Yes, it's an adult")
elif 13 <= userAge <= 17:
    print("Yes, it's a teenager")
else:
    print("Yes, it's a child")


# 22. 7.Write a Python program to remove a key from a dictionary if it is present(3)
# myDict = {&#39;a&#39;:1,&#39;b&#39;:2,&#39;c&#39;:3,&#39;d&#39;:4}

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key = 'c'

# Check if the key exists and remove it
if key in myDict:
    del myDict[key]

print(myDict)

# 23.check a element present in list if not present add that element print new list if it is
# present remove element and print new list

myList = [1, 2, 3, 4, 5]

element = int(input("Enter an element in a list: "))

if element in myList:
    myList.remove(element)
else:
    myList.append(element)

print(myList)

# 24.check a year leap year or not

year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 25. store user name and password of 4 members in a list and create program to login

users = [
    ["roshan", "1234"],
    ["sneha", "abcd"],
    ["akshaykumar", "pass1"],
    ["asinthara", "xyz"]
]

# Take user input
username = input("Enter username: ")
password = input("Enter password: ")

# Check login using if-else
if [username, password] in users:
    print("Login successful!")
else:
    print("Invalid username or password")



# 20. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
# a. Unit Price
# b. First 100 units no charge
# c. Next 100 units Rs 5 per unit
# d. After 200 units Rs 10 per unit
# e. (For example
# if input unit is 350 than total bill amount is Rs2000)



units = int(input("Enter number of units: "))

# Calculate bill using if-else
if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10

# Print total bill
print("Total electricity bill is Rs", bill)



