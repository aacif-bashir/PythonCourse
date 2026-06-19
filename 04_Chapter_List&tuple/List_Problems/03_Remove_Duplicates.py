nums = [12, 21, 2, 3, 14, 4, 5]

result = list(set(nums))
print(result)

# Preserve Order
my_num = []

for i in nums:
    if i not in my_num:
        my_num.append(i)

print(my_num)