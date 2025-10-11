

# ================================================Python Dictionaries==================================================================

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
print(thisDist)

# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates.

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
print(thisDist['course'])


# Duplicates Not Allowed and length

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2027,
    "year":1998
}
print(thisDist)
print(len(thisDist))


# Dictionary Items - Data Types more than two data type can be added by using listr form - type check

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2027,
    "year":1998,
    "location":['calicut','kannur','wayanadu','iddukki']
}
print(thisDist)
print(type(thisDist))

# The dict() Constructor - no need of (()) use dict

thisDist = dict(name = "John", age = 36, country = "Norway")
print(thisDist)

# ===========================================================================Python - Access Dictionary Items=================================

# in order to access the data value by using key following method

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
x= thisDist["course"]
print(x)

# using get method

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
x= thisDist.get("center")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
x=thisDist.keys()
print(x)


# add new key method

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}

x= thisDist.keys()
print(x)
thisDist["location"] = "calicut"
print(thisDist)


# how to aceeses value
thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
Y=thisDist.values()
print(Y)


thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}

x= thisDist.values()
thisDist["year"] =2027
print(x)

 # how add new key and value to folowing Access Dictionary Items
thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
x= thisDist.values()
thisDist["location"]= "calicut"
print(thisDist)


# Get Items

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
x= thisDist.items()
print(x)

# Make a change in the original dictionary, and see that the items list gets updated as well:

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
x= thisDist.items()
print(x)

thisDist["year"] = 2027
print(x)

# to add new 'key' and 'value' to the existing dictionary

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
x= thisDist.items()
print(x)

thisDist["location"]= "calicut"
print(x)

# Check if Key Exists

thisDist= {
    "center":"IPSC",
    "course":"data science",
    "year": 2025
}
if "center" in thisDist:
    print("yes, 'center' is one of the key in the thisDist")

# change values


thisDist ={
"center":"IPSCCCCCCCCCCC",
"course":"data science",
 "year": 2025

}
thisDist["year"]= 2027
thisDist["location"]= "calicut"
thisDist["course"]= "data scienceeeeee"
thisDist["teacher"] = "vidhya"

print(thisDist)

# update mehtod
# Update the "year" of the car by using the update() method:

thisDist= {
"center":"IPSC",
"course":"data science",
 "year": 2025

}
print(thisDist)

thisDist.update({"year":2027})
print(thisDist)


thisDist ={
    "center" : "IPSC",
    "course" : "data science",
    "year": 2025
}
print(thisDist)

thisDist.update({"year":2027,"location":"calicut","facalty":"vidhya mam","time": 2})
thisDist.update({})
print(thisDist)

# ==================================================================ADD ITEMS================================================================
# 1. first method


thisDist ={
"center":"IPSCCCCCCCCCCC",
"course":"data science",
 "year": 2025

}
thisDist["location"]="calicut"
print(thisDist)


# 2. update method

thisDist ={
    "center" : "IPSC",
    "course" : "data science",
    "year": 2025
}
print(thisDist)
thisDist.update({"location":"calicut","facalty":"vidhya mam","time": 2})
print(thisDist)


# ===================================================================REMOVE DICTIONARY=================================================================
# 1.pop mehtod

thisDist ={
    "center" : "IPSC",
    "course" : "data science",
    "year": 2025
}
thisDist.pop("course")
print(thisDist)


# 2.popitem mehtod
# last key and value will get deleted
thisDist ={
    "center" : "IPSC",
    "course" : "data science",
    "year": 2025
}
thisDist.popitem()
print(thisDist)

# 3. delitem method

thisDist ={
    "center" : "IPSC",
    "course" : "data science",
    "year": 2025
}
del thisDist["course"]
print(thisDist)

# 4.del method

# thisDist ={
#     "center" : "IPSC",
#     "course" : "data science",
#     "year": 2025
# }
# del thisDist
# print(thisDist)

# 5. clear Method

thisDist ={
    "center" : "IPSC",
    "course" : "data science",
    "year": 2025
}
thisDist.clear()
print(thisDist)

# ==========================================================COPY METHOD====================================================================

# 1. copy method

thisDist ={
    "center" : "IPSC",
    "course" : "data science",
    "year": 2025
}
thisDist.copy()
print(thisDist)

# 2. dict mehtod

thisDist ={
    "center" : "IPSC",
    "course" : "data science",
    "year": 2025,
    "location": "calicut"
}
dict(thisDist)
print(thisDist)

# ==================================================================Nested Dictionaries=======================================================


# 1. parent child method

myFamily = {
"family1": {
    "name":"xyz",
    "age": 123,
    "year": 2025,
},
    "family2": {
        "name":"abc",
        "age": 456,
        "year": 2026,
    },
    "family3": {
        "name":"pqr",
        "age": 789,
        "year": 2027,
    },
}

print(myFamily)

# 2. child parent method

family1= {
    "name":"xyz",
    "age": 123,
    "year": 2025,
}
family2= {
    "name":"abc",
    "age": 456,
    "year": 2026,
}
family3= {
    "name":"pqr",
    "age": 789,
    "year": 2027,
}
myFamily={
    "family1": family1,
    "family2": family2,
    "family3": family3,
}
print(myFamily)


# Access Items in Nested Dictionaries



family1= {
    "name":"xyz",
    "age": 123,
    "year": 2025,
}
family2= {
    "name":"abc",
    "age": 456,
    "year": 2026,
}
family3= {
    "name":"pqr",
    "age": 789,
    "year": 2027,
}
myFamily={
    "family1": family1,
    "family2": family2,
    "family3": family3,
}

print(myFamily["family1"]["name"])
print(myFamily["family2"]["age"])
print(myFamily ["family3"]["year"])

# ========================================================Dictionary Methods===============================================================================

# 1. fromkeys method

x= {"xyz1","xyz2","xyz3","xyz4","xyz5","xyz6","xyz7","xyz8"}
y=0
thisDist = dict.fromkeys(x,y)
print(thisDist)
