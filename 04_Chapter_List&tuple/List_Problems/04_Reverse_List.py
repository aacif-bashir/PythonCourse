nums = [10, 20, 30, 40, 50]

reverse = nums.reverse()
print("Reversed list is", nums)

# Without Built-in
my_list = [10,20,30,49]
reverse_list = []

for i in range(len(my_list)-1, -1, -1):
    reverse_list.append(my_list[i])

print(reverse_list)