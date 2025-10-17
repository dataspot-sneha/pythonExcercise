# =========================================================Python While Loops========================================


# The while Loop

i=1
while i < 7:
    print("Number 1-7 is:", i)
    i += 1
#
# # The break Statement
#
i=1
while i < 7:
    print("number is break point at 5",i)
    if i == 5:
        break
    i += 1
# #
# # The continue Statement

i = 1
while i < 7:
    i += 1
    if i == 5:
        continue
    print("number break from 5 and continue after 5 ",i)


# else statement
i = 1
while i < 8:
   print("number print from 1 to 7 and after execute else statement",i)
   i += 1
else:
   print("the end")



