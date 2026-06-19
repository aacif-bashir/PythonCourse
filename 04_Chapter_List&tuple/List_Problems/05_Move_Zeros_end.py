nums = [1, 0, 2, 0, 3, 0, 4]

zeros = [0] * nums.count(0)
# print(zeros)

non_zero = [i for i in nums if i != 0]

# print(non_zero)

print(non_zero + zeros)