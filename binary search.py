def binary_search(lst, n):
    flag = False
    first = 0
    last = len(lst) - 1
    mid = 0

    while first <= last:
        mid = (first + last) // 2
        if lst[mid] < n:
            first = mid + 1
        elif lst[mid] > n:
            last = mid - 1
        else:
            return mid
    return -1

        
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter the element to be searched:"))

ans = binary_search(lst, n)
if ans == -1:
    print("Element not found")
else:
    print("Element found at index:", ans)
