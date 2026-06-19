nums = [1, 2, 3, 4, 5]
k = 2

k = k % len(nums) # this is to handle the case when k is greater than the length of the list
print(k)
for i in range(k):
    last = nums.pop()
    nums.insert(0,last)

print(nums)