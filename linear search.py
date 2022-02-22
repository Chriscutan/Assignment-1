n = int(input("Enter size of the list:"))
lst = []

for i in range(0, n):
    lst.append(int(input()))

num = int(input("Number to be searched:"))

for i in range(0, len(lst)):
    if lst[i] == num:
        print(num, "found at", i, "index")
        break
