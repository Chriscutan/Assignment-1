n = int(input("Enter size of the list:"))
lst = []

for i in range(0, n):
    lst.append(input("Enter the element of list:"))

print(lst)
index = int(input("Enter the index to be deleted:"))
lst.pop(index)
print(lst)

