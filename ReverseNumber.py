numbers = int(input("Enter the number: "))
rev = 0
while(numbers > 0):
    rem = numbers % 10
    rev = rev * 10 + rem
    numbers = numbers // 10

print("Your reverse number is:", rev)