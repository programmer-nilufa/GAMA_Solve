
# 1. user input in string
num1 = input ("Enter number :")
print ("type of number", type(num1))

# 2. user input in integer number
num2 = int(input("Enter a number: "))
print(num2, " ", type(num2))

# 3. user input in floating number
floatNum = float(input("Enter a decimal number: "))
print(floatNum, " ", type(floatNum))

# 4. taking inputs at a time uses whitespace
x, y, z = input("Values: ").split()
print(x)
print(y)
print(z)

# 5. Multiple Inputs in One Line
inputs = {i for i in input().split()} # Asking for multiple space-separated values
print(inputs)
print(type(inputs))

x = [int(x) for x in input().split(",")] # taking multiple inputs at a time separated by comma
print(x)
print(type(x))

# 5. Using map() for Multiple Integer Inputs
a = map(int, input().split()) # Take space-separated inputs and convert them to integers
b = list(a) # Convert the map object to a list and print it
print(b)

# Taking Multiple Inputs in a Loop

a = []  # Create an empty list to store the inputs
b = int(input("How many items do you want to enter? "))   # Ask the user for how many items they want to input
for i in range(b): # Loop to collect multiple inputs
    val = input(f"Enter item {i + 1}: ")
    a.append(val)
for i in a:
    print(i)
