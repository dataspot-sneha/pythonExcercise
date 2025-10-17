 # 1. Print numbers from 1 to 10
i = 1
while i <= 10:
    print("the number from 1 to 10",i)
    i += 1

# 2.Print numbers from 10 to 1 (reverse order)

i = 10
while i >= 1:
    print("the number reverse from 1 to 10",i)
    i -= 1

# 3. Find the sum of first 10 numbers

i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum of first 10 numbers is:", total)

# 4.Print even numbers from 1 to 10

i = 1
while i <= 10:
    if i % 2 == 0:
        print("Print even numbers from 1 to 10",i)
    i += 1

# 2. Read a string and print letters

text = input("Enter a string: ")

# Initialize index
i = 0

# Use while loop to print each letter
while i < len(text):
    print(text[i])
    i += 1

# 3. Print the factors of number

num = int(input("Enter a number: "))

i = 1
print(f"Factors of {num} are:")

# Use while loop to find factors
while i <= num:
    if num % i == 0:
        print(i)
    i += 1



numbers = [1, 2, 3, 2, 4, 2, 5]

# Create empty lists for even and odd numbers
even = []
odd = []

# Initialize index
i = 0

# Use while loop to separate numbers
while i < len(numbers):
    if numbers[i] % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
    i += 1

# Print results
print("Even numbers:", even)
print("Odd numbers:", odd)


# 8. find the maximum value and minimum value in the following list
# (without using max and min function) using while loop
# A=[34,56,23,2,12]

A = [34, 56, 23, 2, 12]

i = 1
max_value = A[0]
min_value = A[0]

while i < len(A):
    if A[i] > max_value:
        max_value = A[i]
    if A[i] < min_value:
        min_value = A[i]
    i = i + 1

print("Maximum value:", max_value)
print("Minimum value:", min_value)