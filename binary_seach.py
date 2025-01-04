list1 = []
size = int(input("Enter the list size: "))

for i in range(size):
    data = int(input("data : "))
    list1.append(data)

sort_list = sorted(list1)
print(sort_list)

key = int(input("Enter a key value for search: "))

start = 0
end = len(sort_list)- 1


while(start<=end):

    mid = (start+end)//2

    if sort_list[mid] == key:
        print(f'Your key element is in {mid} index')
        break
    elif sort_list[mid] < key:
        start = mid + 1
    elif sort_list[mid] > key:
        end = mid - 1
    else:
        print("Data not found")

