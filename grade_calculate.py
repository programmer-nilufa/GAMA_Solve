marks = int(input('Enter your marks here: '))
if marks>=101:
    print('Unvalid number')
    exit()
if marks>=90 and marks<=100:
    print('Your Grade A+')
elif marks>=89 and marks<=80:
    print('Your Grade A')
elif marks<=79 and marks>=70:
    print('Your Grade A-')
elif marks<=69 and marks>=60:
    print('Your Grade B')
elif marks<=59 and marks>=50:
    print('Your Grade C')
elif marks<=49 and marks>=33:
    print('Your Grade D')
elif marks<=32 and marks>=0:
    print('You are fail')