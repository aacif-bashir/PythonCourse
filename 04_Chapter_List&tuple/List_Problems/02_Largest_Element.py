
# 1. Find the largest element in a list.

my_list = [10, 8, 2, 8, 1, 3]

my_list.sort()
largest_element = my_list[-1]
print("Largest element is:",largest_element)

# 2. Find the second largest element in a list

print("Second largest element", my_list[-2])

# 3. Find the smallest element in a list.

smallest_element = my_list[0]
print("Smallest element is", smallest_element)


# 4. Calculate the sum of all elements in a list.

sum = 0
for i in my_list:
        sum = sum+i
print("Total sum of elements is", sum)




# 5. Find the average of elements in a list.

average = sum / len(my_list)

print("Average is", average)