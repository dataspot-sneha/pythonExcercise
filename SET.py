
# ===================================================set===================================================================================================

thisSet = {"carrot","potato","tomato"}
# for x in thisSet:
#   print(x)

for y in thisSet:
    print(y)


thisSet = {"carrot","potato","tomato"}
print("tomato" in thisSet )

thisSet = {"carrot","potato","tomato"}
print("tomato" not in thisSet )

# new element add to set -insert method
# 1. add method

thisSet = {"carrot","potato","tomato"}
thisSet.add("chilly")
print(thisSet)

# 2. update method
thisSet = {"carrot","potato","tomato"}
updateSet = {"apple","banana","orange"}
thisSet.update(updateSet)
print(thisSet)

thisSet = {"carrot","potato","tomato"}
updateSet = ["apple","banana","orange"]
thisSet.update(updateSet)
print(thisSet)



 # element removing from the set - remove method

 # 1. remove method

thisSet = {"carrot","potato","tomato"}
thisSet.remove("potato")
print(thisSet)

# 2. discard method

thisSet = {"carrot", "potato", "tomato"}
thisSet.discard("potato")
print(thisSet)

# 3.pop method

thisSet = {"carrot", "potato", "tomato"}
x= thisSet.pop()
print(x)
print(thisSet)

# 4.clear method

thisSet = {"carrot", "potato", "tomato"}
thisSet.clear()
print(thisSet)

# 5.delete method

thisSet = {"carrot", "potato", "tomato"}
del thisSet
