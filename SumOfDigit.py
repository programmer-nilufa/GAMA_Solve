number = int(input())
sum = 0
while(number > 0):
    rec = number % 10
    sum += rec
    number = number // 10

print(sum)


    