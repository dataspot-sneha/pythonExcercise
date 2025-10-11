# ============================================================= VALUTION 2 ============================================================================================

# 1.1.Write a program that removes whitespace from the following strings,
# then print out the strings with the whitespace removed:
# string1 ="         Filet Mignon&quot";
# string2 =" Brisket &quot";
# string3 = "         Cheeseburger"


string1 ="         Filet Mignon&quot"
string1 = string1.strip()
print(string1)


string2 =" Brisket       "
string2=string2.strip()
print(string2)

string3 = "              Cheeseburger "
string3=string3.strip()
print(string3)


# 2.2. Write a program that takes input from the user and displays the input
# in uppercase.

course = input("Enter your course: ")
print(course.upper())
print(type(course))

# 3.3. Write a program that takes input from the user and displays the
# number of characters in the input.

location= input("Enter your location: ")
location = str(len(location))
print("The number of characters in the input is:", location)


# 4.Write a program that uses input() twice to get two numbers from the
# user, multiplies the numbers together, and displays the result. If the user
# enters 2 and 4, then your program should print the following text:
#
# Output: The product of 2 and 4 is 8.0

int1 = float(input("Enter first number:"))
int2 = float(input("Enter second number:"))
product = int1 * int2
print(f"Output: The product of {int1} and {int2} is {product}")

# 5.Create a float object named weight with the value 0.2, and create a
# string object named animal with the value &quot;newt&quot;. Then use these
# objects to print the following string using only string concatenation:
# Output: 0.2 kg is the weight of the newt.

weight = 0.2
animal = "newt"

print("output:  " +(str(weight) + " kg is the weight of the " + animal ))



# 6. Display the same string by using .format() and empty {} placeholders.
weight = 0.2
animal = "newt"

print("output:   "  +"{} kg is the weight of the {}.".format(weight, animal))

# 7.Display the same string using an f-string

weight = 0.2
animal = "newt"

print("output:   "  +f"{weight} kg is the weight of the {animal}.")

# 8.How to add values to a python list?

List = [1, 2, 3]
List.append(4)
print(List)

# two list joining using extend
List = [1, 2, 3]
fruit = ["banana","orange","apple"]
List.extend(fruit)
print(List)


# 9.What will the following code output?
# Word=’abcdefghij’
# Word[:3]+word[3:]


Word="abcdefghij"
print(Word[:3])
print(Word[3:])

# 10How will you remove a duplicate element from a list?
# List=[1,2,1,3,4,2]

List=[1,2,1,3,4,2]
List.remove(1)
print(List)


# 11.11.Write a Python program to add member(s) in a set.

vegetable = {"carrot","beetroot","onion","chilly"}
newVegetable =("potato")
vegetable.add(newVegetable)
print(vegetable)

# 12.Write a Python program to remove an item from a set if it is present in
# the set

set= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
if "center" in set:
    print("yes, 'center' is one of the key in the set")

# 13.Write a Python program to create an intersection of sets
# setx = set([&quot;green&quot;, &quot;blue&quot;])
# sety = set([&quot;blue&quot;, &quot;yellow&quot;])

setx = {"green", "blue"}
sety = {"blue", "yellow"}
setz= setx.intersection(sety)
print("Intersection of sets:", setz)

# 14.Write a Python program to remove all elements from a given set.

set = {1, 2, 3, 4, 5}

print("Original Set:", set)
set.clear()

print("Set after removing all elements:",set)


# 15.Write a Python script to add a key to a dictionary
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dict = {0: 10, 1: 20}

print("Original Dictionary:", dict)
dict[2] = 30

print("Updated Dictionary:", dict)


# 16.Write a Python program to concatenate following dictionaries to
# create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = dic1 | dic2 | dic3
print(new_dict)

#
# 17.Write a Python program to check whether a given key already exists
# in a dictionary.


dictKey = {1: 10, 2: 20, 3: 30}
key = 2
if key in dictKey:
    print(f"Key {key} exists in the dictionary.")


# 18.Write a Python program to remove a key from a dictionary

number = {1: 10, 2: 20, 3: 30, 4: 40}
number.pop(2)
print("After removing key 2:", number)


# 19.Write a Python program to combine two dictionary adding values for
# common keys
# d1 = {&#39;a&#39;: 100, &#39;b&#39;: 200, &#39;c&#39;:300}
# d2 = {&#39;a&#39;: 300, &#39;b&#39;: 200, &#39;d&#39;:400}

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = d1.copy()
for key in d2:
    if key in result:
        result[key] = result[key] + d2[key]

print("Combined Dictionary:", result)

# 20.create list using following dictionary
# d1 = {&#39;a&#39;: 100, &#39;b&#39;: 200, &#39;c&#39;:300}
# d2 = {&#39;a&#39;: 600, &#39;b&#39;: 400, &#39;d&#39;:500}
# expected output:[100,200,300,400,500,600]

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 600, 'b': 400, 'd': 500}

# Take values from both dictionaries
result = list(d1.values()) + list(d2.values())

print("Resulting List:", result)


# 21.Write a Python program to find no of pairs in dict
# {&#39;a&#39;: 5, &#39;b&#39;: 14, &#39;c&#39;: 32, &#39;d&#39;: 35, &#39;e&#39;: 24, &#39;f&#39;: 100, &#39;g&#39;: 57, &#39;h&#39;: 8, &#39;i&#39;: 100}


my_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}

count = 0
for value in my_dict.values():
    if value % 2 == 0:
        count += 1
print("Number of pairs (even numbers) in dictionary:", count)

# 22.Write a Python program to unpack a tuple in several variables.

tuple = (10, 20, 30)

a, b, c = tuple

print("a:", a)
print("b:", b)
print("c:", c)

# 23.Write a Python program to convert a tuple to a string.
# tup = ('p', 'y', 't', 'h', 'o', 'n')

tup = ('p', 'y', 't', 'h', 'o', 'n')
result = ''.join(tup)
print("Converted String:", result)

# 24.Write a Python program to get the 4th element from last of a tuple.
# A=(1,”a”,2,”b”,3,”c”,4,”d”,5,”e”,6,”f”,7)

A = (1, "a", 2, "b", 3, "c", 4, "d", 5, "e", 6, "f", 7)
result = A[-4]

print("4th element from last:", result)


# 25.Write a Python program to remove ‘o’ from a tuple
# tup = ('p','y','t','h','o','n')
#
# tup = ('p', 'y', 't', 'h', 'o', 'n')
# newTup = list(tup)
# newTup.remove('o')
# print(newTup)
# tup = tuple(newTup)


# 5.Change Plato&#39;s birth year from 427 to 428(2)
# dict={&quot;name&quot;: &quot;Plato&quot;, &quot;country&quot;: &quot;Ancient Greece&quot;, &quot;born&quot;: -427, &quot;teacher&quot;:
# &quot;Socrates&quot;, &quot;student&quot;: &quot;Aristotle&quot;}


dict = {
"name": "Plato",
"country": "Ancient Greece",
"born": -427,
"teacher": "Socrates",
"student": "Aristotle"
}

# Change birth year
dict["born"] = -428

print(dict)

# Write a Python program to access dictionary key&#39;s element by index.(3)
# num = {&#39;physics&#39;: 80, &#39;math&#39;: 90, &#39;chemistry&#39;: 86}

num = {'physics': 80, 'math': 90, 'chemistry': 86}

key = list(num)[1]
value = num[key]

print("Key:", key)
print("Value:", value)

# .Write a Python program to concatenate elements of a list. (2)
# color = [&#39;red&#39;, &#39;green&#39;, &#39;orange&#39;]
# output: red-green-orange

color = ['red', 'green', 'orange']
result = '-'.join(color)
print(result)


# Write a Python program to find the length of a set.(1)
# setn = {5, 5, 5, 5, 5, 5}

setn = {5, 5, 5, 5, 5, 5}
print(len(setn))


# write examples for functions lower(),upper(),strip(),format()

text = "Hello WORLD"
print(text.lower())


text = "Hello world"
print(text.upper())

text = "   Python Programming   "
print(text.strip())

name = "Data Science"
age = 50
print("My name is {} and I am {} years old.".format(name, age))

# Write a Python program to remove all elements from a given set.(1)
# setc = {&quot;Red&quot;, &quot;Green&quot;, &quot;Black&quot;, &quot;White&quot;}

setc = {"Red", "Green", "Black", "White"}

# Remove all elements
setc.clear()

print(setc)


#
# . Write a Python program to remove duplicates from a list.(2)
# a = [10,20,30,20,10,50,60,40,80,50,40]

# a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# a.remove(10)

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Remove duplicates
a = list(set(a))

print(a)



# Write a Python program to convert a list into a string.(2)
# l=[&quot;data&quot;,&quot;science&quot;,&quot;python&quot;,&quot;fullstack&quot;]
# output: data-fullstack-python-science

l = ["data", "science", "python", "fullstack"]

l = ["data", "fullstack", "python", "science"]

result = '-'.join(l)
print(result)

# Check if a value 200 exists in a dictionary(2)
# sampleDict = {&#39;a&#39;: 100, &#39;b&#39;: 200, &#39;c&#39;: 300}

sampleDict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sampleDict.values():
    print("Value 200 exists in the dictionary")

# Create a tuple with single item 50

tuple = (50)
print(tuple)
print(type(tuple))
#
# Write a python program to find the common numbers from two lists(2)
# A=[1,20,3,4,5]
# B=[20,100,3,23,78]

A = [1, 20, 3, 4, 5]
B = [20, 100, 3, 23, 78]

# Using list comprehension to find common numbers
common_numbers = [num for num in A if num in B]

print("Common numbers:", common_numbers)


# Given a Python list, find value 20 in the list, and if it is present, replace it with
# 200. Only update the first occurrence of a value(3)
# list1 = [5, 10, 15, 20, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]

# Check if 20 is in the list
if 20 in list1:
    print("Value 20 exists in the list 1")
    index = list1.index(20)
    print(index)
    list1[index] = 200       # Replace it with 200
print(list1)

# Add a list of elements to a given set(2)
# sampleSet = {&quot;Yellow&quot;, &quot;Orange&quot;, &quot;Black&quot;}
# sampleList = [&quot;Blue&quot;, &quot;Green&quot;, &quot;Red&quot;]

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

sampleSet.update(sampleList)
print(sampleSet)

# Returns a new set with all items from both sets by removing duplicates(2)
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result = set1.union(set2)
print(result)

# Returns a new set with all items from both sets by removing duplicates(2)
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result = set1|set2
print(result)

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Remove duplicates
a = list(set(a))

print(a)

print("======================================================",a)



list1 = [5, 10, 15, 20, 25, 50, 20]
#
# Check if 20 is in the list
if 20 in list1:
    print("Value 20 exists in the list 1")
    index = list1.index(20)
    print(index)
    list1[index] = 200       # Replace it with 200
# print(list1)

tup = ('p','y','t','h','o','n')

tup = ('p', 'y', 't', 'h', 'o', 'n')
newTup = list(tup)
newTup.remove('o')
print(newTup)
tup = tuple(newTup)