# 1. String
# Creating a String
s = "GfG"
print(s[1]) # access 2nd char
s1 = s + s[0] # update
print(s1) # print

#Multi-line Strings
s2 = """I am Learning
Python String on GeeksforGeeks"""
print(s2)

# Accessing characters in Python String
s3 = "GeeksforGeeks"
print(s3[0])   # Accesses first character: 'G'
print(s3[4])   # Accesses 5th character: 's'

# Access string with Negative Indexing
s4 = "GeeksforGeeks"
print(s4[-10])  # Accesses 3rd character: 'k'
print(s4[-5])   # Accesses 5th character from end: 'G'

# String Slicing
s5 = "GeeksforGeeks"
print(s5[1:4])  # Retrieves characters from index 1 to 3: 'eek'
print(s5[:3])  # Retrieves characters from beginning to index 2: 'Gee'
print(s5[3:])   # Retrieves characters from index 3 to the end: 'ksforGeeks'
print(s5[::-1])  # Reverse a string

# String Immutability
s6 = "geeksforGeeks"
# Trying to change the first character raises an error
# s[0] = 'I'  # Uncommenting this line will cause a TypeError
# Instead, create a new string
s6 = "G" + s6[1:]
print(s6)

# Deleting a String
s7 = "GfG"
del s7 # Deletes entire string

# Updating a String
s8 = "hello geeks"
s1111 = "H" + s8[1:]  # Updating by creating a new string
s2222 = s8.replace("geeks", "GeeksforGeeks") # replacnig "geeks" with "GeeksforGeeks"
print(s1111)
print(s2222)

# Replaces a String
s9 = "   Gfg   "
print(s9.strip())  # Removes spaces from both ends
s9 = "Python is fun"
print(s9.replace("fun", "awesome"))  # Replaces 'fun' with 'awesome'

# Repeating Strings
s10 = "Hello "
print(s10 * 3)

# Formatting Strings
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")

# Using format()
s11 = "My name is {} and I am {} years old.".format("Alice", 22)
print(s11)

#Using in for String Membership Testing
s12 = "GeeksforGeeks"
print("Geeks" in s12)
print("GfG" in s12)


# 2. Number
# Arithmetic Operations on int type
# Integer

# Addition
print(res1 = 5 + 3 )   # Output: 8

# Subtraction
res = 10 - 4   # Output: 6

# Multiplication
res = 7 * 6    # Output: 42

# Division
res = 15 / 4   # Output: 3.75

# Floor Division
res = 15 // 4  # Output: 3

# Modulus (%)
res = 15 % 4   # Output: 3 (because 15 divided by 4 gives remainder 3)

# Exponentiation (**)
res = 2 ** 3   # Output: 8 (because 2 raised to the power of 3 is 8)

# Absolute Value (abs)
res = abs(-10) # Output: 10 (absolute value of -10)

# Round (round)
res = round(3.14159, 2)  # Output: 3.14 (rounds to 2 decimal places)

# Floating
# Addition (float)
res = 3.5 + 2.2   # Output: 5.7

# Subtraction (float)
res = 7.8 - 4.3   # Output: 3.5

# Multiplication (float)
res = 5.5 * 2.0   # Output: 11.0

# Division (float)
res = 9.0 / 4.5   # Output: 2.0

# Floor Division (float)
res = 9.0 // 4.5  # Output: 2.0 (it returns the truncated quotient)

# Modulus (%) (float)
res = 9.0 % 4.5   # Output: 0.0 (remainder when divided)

# Exponentiation (float)
res = 2.5 ** 2    # Output: 6.25 (2.5 raised to the power of 2)

# Absolute Value (float)
res = abs(-7.4)   # Output: 7.4 (absolute value)

# Round (float)
res = round(3.14159, 2)  # Output: 3.14 (rounds to 2 decimal places)


# Python Complex
# Addition (complex)
res = (3 + 4j) + (1 + 2j)   # Output: (4 + 6j)

# Subtraction (complex)
res = (5 + 6j) - (2 + 3j)   # Output: (3 + 3j)

# Multiplication (complex)
res = (2 + 3j) * (1 + 4j)   # Output: (-10 + 11j)

# Division (complex)
res = (8 + 6j) / (2 + 3j)   # Output: (2.0 + 0.0j)

# Exponentiation (complex)
res = (1 + 1j) ** 2    # Output: (0 + 2j) (raises the complex number to the power of 2)

# Absolute Value (complex)
res = abs(3 + 4j)   # Output: 5.0 (absolute value of a complex number, which is sqrt(3^2 + 4^2))

# Conjugate of a complex number
res = (3 + 4j).conjugate()   # Output: (3 - 4j) (negates the imaginary part)

# Real and Imaginary parts of a complex number
real = (3 + 4j).real   # Output: 3.0
imag = (3 + 4j).imag   # Output: 4.0


# Random Numbers
# Generating Random Integer
import random
x = random.randint(1, 100)
print(x)

# Generating Random FLoating Point Integer
x = random.uniform(1.0, 10.0)
print(x)


# Special Numbers in Python
# NaN Example
import math
n = math.nan
print(n)

# Infinity and -Infinity Example
x = float('inf')
y = float('-inf')
print(x)
print(y)


# Python Boolean
# or, and
a = 0
b = 2
c = 4
if a > b and b < c:
    print(True)
else:
    print(False)

if a and b and c:
    print("True")
else:
    print("False")

# not
a = 0
if not a:
    print("False")

# Boolean == (equivalent) and != (not equivalent) Operator
a = 0
b = 1
if a == 0:
    print(True)
if a == b:
    print(True)
if a != b:
    print(True)

# Python is Operator
x = 10
y = 10
if x is y:
    print(True)
else:
    print(False)

# Python in Operator
a = [1, 2, 2]  # Create a list
if 1 in a:  # Check if lion in list or not
    print(True)



# 3. List
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types
print(a)
print(b)
print(c)

# Using list() Constructor
a = list((1, 2, 3, 'apple', 4.5))  # From a tuple
print(a)

# Creating List with Repeated Elements
a = [2] * 5 # Create a list [2, 2, 2, 2, 2]
b = [0] * 7  # Create a list [0, 0, 0, 0, 0, 0, 0]
print(a)
print(b)

#  Accessing List Elements
a = [10, 20, 30, 40, 50]
print(a[0])    # Access first element
print(a[-1])  # Access last element

# Adding Elements into List (append(), extend(), insert())
a = []  # Initialize an empty list
a.append(10)  # Adding 10 to end of list
print("After append(10):", a)

a.insert(0, 5) # Inserting 5 at index 0
print("After insert(0, 5):", a)

a.extend([15, 20, 25]) # Adding multiple elements  [15, 20, 25] at the end
print("After extend([15, 20, 25]):", a)


# Removing Elements from List
a = [10, 20, 30, 40, 50]
a.remove(30)  # Removes the first occurrence of 30
print("After remove(30):", a)

popped_val = a.pop(1)  # Removes the element at index 1 (20)
print("Popped element:", popped_val)
print("After pop(1):", a)

del a[0]  # Deletes the first element (10)
print("After del a[0]:", a)


# Iterating Over Lists
a = ['apple', 'banana', 'cherry']
for item in a:   # Iterating over the list
    print(item)


# Nested Lists in Python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Access element at row 2, column 3

# Length of a List
# Using len()
a = [1, 2, 3, 4, 5]
length = len(a)
print(length)

# Using loop (Naive method)
a = [1, 2, 3, 4, 5]
count = 0  # Initialize a counter to zero
for val in a:   # Loop through each element in the list
    count += 1  # Increment the counter for each element
print(count)