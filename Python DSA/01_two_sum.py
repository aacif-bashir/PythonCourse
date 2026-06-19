# Problem
# Given an array of numbers and a target, return indices of two numbers whose sum equals the target.
# nums = [2, 7, 11, 15]
# target = 9

# Output:
# [0, 1]


nums = [2, 7, 11, 15]
target = 9

# Approach 1: Brute Force
n = len(nums)
for i in range(n):
    for j in range(i+1, n):
        if nums[i]+ nums[j] == target:
            print([i,j])
            break

# Approach 2:  Using enumerate (Nested Loops)
for index1, data1 in enumerate(nums):
    for index2, data2 in enumerate(nums[index1+1:], start = index1+1):
        if data1 + data2 == target:
            print([index1, index2])
            break


# Optimal Approach: Hash Map (Dictionary)

seen = {}  # Dictionary to store the numbers and their indices

for i, number in enumerate(nums): # Iterate through the list with index and number
    complement = target - number  # Calculate the complement that we need to find
    if complement in seen:        # Check if the complement is already in the seen dictionary
        print([seen[complement],i]) # If it is, we found the two numbers that add up to the target, so we print their indices
        break
    seen[number] = i  # Store the number and its index in the dictionary