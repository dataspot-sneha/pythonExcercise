#                                        Python If ... Else

# 1 if condition

a=50
b=20
if a>b:
    print("a is greater than b")


# 2. elif condition

a=20
b=20
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")


# 3.if elif and else conditon

a=50
b=60
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than b")



# 4short hand if
a=500
b=60
if a>b:(print("a is greater than b"))

# 5short hand if elae

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# and conditon

a = 3300
b = 390
c = 4000
if a > b and c > a:
    print("a is greater than b")

# or condition

a = 3300
b = 330
c= 5000
if a > b or c > a:
    print("a is greater than b")
#
# not condition

a = 3
b = 330
if not a > b:
    print(" a is not greater than b")


# Nested If

R= 100

if R > 20:
    print("R is greater than 20")
if R > 30:
    print("R is greater than 30")
if R < 2:
    print("R is less than 2")
else:
    print("R is eqaul to 100")

# pass in if condition:==================================================================IMPORTANT

# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.

a= 20
b= 20
if a > b:
    pass







