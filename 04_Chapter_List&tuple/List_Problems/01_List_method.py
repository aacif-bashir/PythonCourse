
# Append: adds an item to the end of the list

my_list = ["aasif", 12, "python", 3.14]

my_list.append("new item")

print("Append", my_list)
# Extend: adds multiple items from an iterable to the end of the list

my_list.extend(["Extend one", "Extend", 2])

print("Extend", my_list)

#Insert: Inserts an item at a specified index. 

my_list.insert(0,"Inserted at 0")

print("Insert Method",my_list)

# Remove: Removes the first occurrence of an item

my_list.remove("python")

print("Remove Method",my_list)


# POP: Removes and returns the item at the specified index. If no index is specified, removes and returns the last item in the list.
pop_item = my_list.pop(2)
print("POP Method", my_list)
print("Popped Item", pop_item)

# Clear: Removes all items from the list
my_list.clear()
print("Clear Method", my_list)