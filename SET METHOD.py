
# =========================================================SET METHODS==============================================================================

# 1. add method

thisSet = {"carrot", "potato", "tomato"}
thisSet.add("chilly")
print(thisSet)

# 2. clear method

thisSet = {"carrot", "potato", "tomato"}
thisSet.clear()
print(thisSet)

# 3.copy method

thisSet = {"carrot", "potato", "tomato"}
x= thisSet.copy()
print(x)

# 4.difference method

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
resultSet = thisSet.difference(defSet)
print(resultSet)

 # difference using - symbol

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
resultSet = thisSet- defSet
print(resultSet)

# 5.difference_update()

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
thisSet.difference_update(defSet)
print(thisSet)

# 5.difference_update() using symbol  -=
thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
thisSet -= defSet
print(thisSet)

# 5.morethan two set how to find difference

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
a.difference_update (b,c)
print(a)


# 5.morethan two set how to find difference using symbol


a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}

a -= b|c
print(a)

# 6. discard method
thisSet = {"carrot", "potato", "tomato"}
thisSet.discard("potato")
print(thisSet)

# 7. intersection method

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
resultSet = thisSet.intersection(defSet)
print(resultSet)

# 8. intersection method using symbol

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
resultSet= thisSet & defSet
print(resultSet)

# 9. intersection method more tha two sets
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)

# 10. intersection method more tha two sets using symbols

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x & y & z

print(result)

# 11.  intersection_update method

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
thisSet.difference_update(defSet)
print(thisSet)

# 12.  intersection_update method using symbol
thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
resultSet &= defSet
print(resultSet)

# 13.intersection_update method for than two sets

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.difference_update(y,z)
print(x)

# 13.intersection_update method for than two sets by symbols

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x &= y & z
print(x)

# 14.Set isdisjoint result will be true or false

# 1.false case
thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","carrot"}
resultSet = thisSet.isdisjoint(defSet)
print(resultSet)


# 2. true case
thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange"}
resultSet = thisSet.isdisjoint(defSet)
print(resultSet)


# 15. issubset
thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato", "tomato"}
resultSet = thisSet.issubset(defSet)
print(resultSet)
# ===============return result true

# 16. issubset symbol

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato", "tomato"}
resultSet = thisSet <= defSet
print(resultSet)
# ===========================================================================================return result true

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
resultSet = thisSet <= defSet
print(resultSet)
# ============================================================================================returns result false

# 17.issuperset()

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato", "tomato"}
resultSet = thisSet.issuperset(defSet)
print(resultSet)
# ==========================================================================================return resukt true

# 18.issuperset() using symbol

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato","tomato"}
resultSet = thisSet >= defSet
print(resultSet)
# ================================================================================================return result true

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
resultSet = thisSet.issuperset(defSet)
print(resultSet)

# ====================================================================================================return false

# 19.pop method
thisSet = {"carrot", "potato", "tomato"}
thisSet.pop ()
print(thisSet)

# =======================================any element from the set can be poped not a particular element

fruits = {"carrot", "potato", "tomato"}
defpop = fruits.pop()
print(defpop)

# =========================================================================================first element will get poped

# 20.remove

thisSet = {"carrot", "potato", "tomato"}
thisSet.remove("carrot")
print(thisSet)

# 21.Set symmetric_difference() Method
#
# will remove the same element of two set and gives the result


thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
resultSet = thisSet.symmetric_difference(defSet)
print(resultSet)

# 22.Set symmetric_difference() Method using symbol

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
resultSet = thisSet^defSet
print(resultSet)

# 23.Set symmetric_difference_update() Method

# will remove the same element of two set and gives the result

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
thisSet.symmetric_difference_update(defSet)
print(thisSet)


# 24. union of set

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
resultSet = thisSet.union(defSet)
print(resultSet)

# 25. union of set using symbol

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
resultSet = thisSet| defSet
print(resultSet)

# 26. union of set with more than two sets

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y,z)
print(result)

# 27. union of set with more than two sets by using symbols

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x|y|z
print(result)

# 28. update method of set
# update the two into one set and remove the same element from the set

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
thisSet.update(defSet)
print(thisSet)


# 29.update method of set using symbol

thisSet = {"carrot", "potato", "tomato"}
defSet = {"apple","banana","orange","carrot", "potato"}
thisSet|=defSet
print(thisSet)


# 30.update method of set more than two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}

x.update(y,z)
print(x)


# 31.update method of set more than two sets using symbol

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}

x |= y | z
print(x)