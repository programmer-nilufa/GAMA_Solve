number = input('Enter the number here: ')
numbers = number.split()

count = 0
for i in numbers:
    count+=1

for j in range(count):
    numbers[j] = int(numbers[j])
print(numbers)


print('The sorted number is :',sorted(numbers))

start = numbers[0]
end = numbers[]
print(f'The start number and end number is {start,end}')








