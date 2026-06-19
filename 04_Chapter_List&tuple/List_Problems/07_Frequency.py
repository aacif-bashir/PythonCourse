# Frequency means how many times an element appears in a list.

nums = [10, 20, 10, 30, 20, 10]

freq = {}

for i in nums:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

print(freq)

# for single element 

fre = nums.count(10)
print("Frequency of 10 is", fre)