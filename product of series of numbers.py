nums = input()
nums = nums.split(" ")

for i in range(0, len(nums)):
    nums[i] = float(nums[i])

prod = 1
for i in nums:
    prod = prod * i

print(prod)
