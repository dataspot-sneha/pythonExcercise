# ----------------------------------------------LIST--------------------------------------------important
# use []to print list

testlist=["test1, test2, test3"]
print(testlist)

# allows duplication in list
testlist=["test1, test2, test3, test1"]
print(testlist)
print(len(testlist))

# to find length of list indexing in python-------------------------------------------0,1,2, index numbering

testlist=["test1", "test2", "test3", "test1"]
print(len(testlist))
print(type(testlist))

testlist=(("test1", "test2", "test3", "test1"))
print(testlist)
# The list() Constructor

testlist= list(("test1", "test2", "test3", "test1"))
print(testlist)


# Access Items
# index numbering

veglist=["carrot","tomato","chilly","ladiesfinger","potato","cabbage"]
print(veglist[1])
print(veglist[5])
print(veglist[1:5])
print(veglist[2:])
print(veglist[:5])
print(veglist[-5:-1])
print(veglist[:-5])
print(veglist[-3:])

# Check if Item Exists----------------------------------------------------------------------no else condition in this

veglist=["carrot","tomato","chilly","ladiesfinger","potato","cabbage"]
if "carrot" in veglist:
    print("yes 'carrot' is in vegetable list")


# Change List Items
veglist=["carrot","tomato","chilly","ladiesfinger"]
veglist[3]= "onion"
print(veglist)


veglist1=["carrot","tomato","chilly","ladiesfinger"]
veglist1[2:3]= ["potato","cabbage"]
print(veglist1)


veglist2=["carrot","tomato","chilly"]
veglist2[1:2]= ["onion","potato","cabbage"]
print(veglist2)

veglist3=["carrot","tomato","chilly"]
veglist3[1:3] = "cabbage"
print(veglist3)

veglist3=["carrot","tomato","chilly"]
veglist3[1:3] = ["cabbage"]
print(veglist3)

veglist4=["carrot","tomato","chilly","ladiesfinger"]
veglist4[6:3] = ["cabbage","onion"]
print(veglist4)

veglist4=["carrot","tomato","chilly","ladiesfinger"]
print(veglist4)

# change list items
# Append Items

veglist=["carrot","beetroot","chilly"]
veglist.append("onion")
print(veglist)

veglist=["carrot","beetroot","chilly","tomato"]
veglist.insert(2,"potato")
print(veglist)

veglist=["carrot","beetroot","chilly"]
listveg=["tomato","ladiesfinger","potato"]
veglist.extend(listveg)
print(veglist)

veglist=["carrot","beetroot","chilly"]
listveg=("tomato","ladiesfinger","potato")
veglist.extend(listveg)
print(veglist)


# remove list items

# Remove Specified Item

veglist=["carrot","chilly","potato"]
veglist.remove("chilly")
print(veglist)

veglist=["carrot","chilly","potato"]
veglist.pop(0)
print(veglist)

veglist=["carrot","chilly","potato","chilly"]
veglist.remove("chilly")
print(veglist)

veglist=["carrot","chilly","potato"]
veglist.pop()
print(veglist)

veglist=["carrot","chilly","potato"]
del veglist[1]
print(veglist)

veglist=["carrot","chilly","potato"]
del veglist

veglist=["carrot","chilly","potato"]
veglist.clear()
print(veglist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# sort method
veglist=["carrot","chilly","potato"]
veglist.sort()
print(veglist)

number=[2,4,5,68,8,9,900,0]
number.sort()
print(number)

veglist=["carrot","chilly","potato"]
veglist.sort(reverse=True)
print(veglist)

veglist=["carrot","chilly","potato"]
veglist.reverse()
print(veglist)

number=[2,4,5,68,8,9,900,0]
number.sort(reverse=True)
print(number)

# copy list

veglist=["carrot","chilly","potato","chilly"]
newlist=veglist.copy()
print(newlist)

veglist=["carrot","chilly","potato","chilly"]
newlist=list(veglist)
print(newlist)

veglist=["carrot","chilly","potato","chilly"]
newlist=veglist[:]
print(newlist)

# join list

testlist=["test1","test2","test3","test4"]
numlist=[1,2,3,4,5,6,7,8,9,10]
finallist=testlist+numlist
print(finallist)

testlist=["test1","test2","test3","test4"]
numlist=[1,2,3,4,5,6,7,8,9,10]
testlist.extend(numlist)
print(testlist)

#