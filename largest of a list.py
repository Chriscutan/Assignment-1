n = int(input("Enter size of the list:"))
lst = []

for i in range(0, n):
    lst.append(int(input()))

largest = 0
for i in range(0, len(lst)):
    if lst[i] > largest:
        largest = lst[i]

print(largest)

    
