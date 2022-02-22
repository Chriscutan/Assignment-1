lst = []

for i in range(10):
    lst.append(int(input("Enter numbers in list:")))

j = 0
total = 0
while j != 10:
    total = total + lst[j]
    j += 1

avg = total/10

print("Average is:",avg)
