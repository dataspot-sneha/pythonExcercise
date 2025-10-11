#==========================================tuple method=========================================================================================

vegList= ("carrot","chilly","tomato")
# while inserting new element to tuple using + operator element should be separated using comma
newVegList = ("potato",)
vegList += newVegList
print(vegList)


#remove tuple method
vegList= ("carrot","chilly","tomato")
newVegList = list(vegList)
newVegList.remove("tomato")
print(newVegList)
vegList= tuple(newVegList)
print(vegList)


# del tuple method
vegList= ("carrot","chilly","tomato")
# note: no need of () while calling delete method
del vegList
# print(vegList)

# Unpacking a Tuple

vegList= ("carrot","chilly","tomato")
# while assiging new elements dont want to be decalred as string
(orange,green,red)=vegList
print(orange)
print(green)
print(red)

# Unpacking a Tuple using *

veglist=["carrot","tomato","chilly","ladiesfinger","potato","cabbage"]
(orange, green ,*red)= veglist
print(orange)
print(green)
print(red)

veglist=["carrot","tomato","chilly","ladiesfinger","potato","cabbage"]
(orange, *green ,red)= veglist
print(orange)
print(green)
print(red)

# Tuples
# same in form of list
# tuples are unchangable
#
# update - tuple using index numbering

X = ("carrot","chilly","tomato")
Y =list(X)
print(Y)
Y[2]="potato"
X=tuple(Y)
print(X)



# insert - tuple append method

vegList= ("carrot","chilly","tomato")
newVegList =list(vegList)
print(newVegList)
newVegList.append("potato")
vegList=tuple(newVegList)
print(vegList)
