numbers = int(input("Enter the number: "))
rev = 0
num = numbers
while(numbers > 0):
    rem = numbers % 10
    rev = rev * 10 + rem
    numbers = numbers // 10

if num == rev:
    print(f"Yes \nThis valuse is palindrom ")
else: print(f"No \nThis valuse is not palindrom ")
