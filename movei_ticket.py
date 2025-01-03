days = input('Enter the day: ')
day = days.lower()
# day_len = len(day)
age = int(input('Enter your age: '))
if day=='wednesday':
    if age<18:
        discount = 8-2
        print(f'{discount} for Child')
    else:
        discount = 12-2
        print(f'{discount} for Adult')
else:
    if age<18:
        print('$8 for Child')
    else:
        print('$12 for Adult')