num1 = int(input("Enter the frist number: "))
num2 = int(input("Enter the Second number: "))
oparator = input("Enter the oparetor (+, -, *, /) :")

if oparator == '+':
    num = num1 + num2
elif oparator == '-':
    num = num1 - num2
elif oparator == '*':
    num = num1 * num2
elif oparator == '/':
    if oparator != 0:
        num = num1/num2
    else: print("Numer is divided by zero")
else: print("Invalid Oparators ")

print(num)