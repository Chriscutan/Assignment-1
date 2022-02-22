dictionary = {}

n = int(input("Enter size of dictionary:"))

for i in range(0, n):
    key = input("Enter the key:")
    value = input("Enter the value:")
    dictionary[key] = value

print(dictionary)
