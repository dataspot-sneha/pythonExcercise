#
                                       # FOR LOOP
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

vegetables = ["carrot","onion","potato","tomato"]
for x in vegetables:
    print(x)

# Looping Through a String

for x in "potato":
    print("looping through a string",x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

vegetables = ["carrot","onion","potato","tomato"]
for x in vegetables:
    print("without break point",x)
    if x=="potato":
        break

# the break statement without including breaking point

vegetables = ["carrot","onion","potato","tomato"]
for x in vegetables:
  if x == "potato":
    break
  print(x)

