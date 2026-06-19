"""
A list in python is an ordered, mutable collection used to store multiple items/values in a single variable.

Key features:
1. Ordered: The items in a list have a defined order, and that order will not change unless you explicitly reorder the list.
2. Mutable: You can change, add, or remove items from a list after it has been created.
3. Allows Duplicates: Lists can contain multiple instances of the same value.
4. Dynamic Size: Lists can grow and shrink in size as needed.
5. Heterogeneous: Lists can contain items of different data types.

"""

fruit_list = ["Apple", "Banana", "Orange", "Mango", "Peach"]

#List Indexing
print(fruit_list[0])  # Accessing the first item
print(fruit_list[1])  # Accessing the second item
print(fruit_list[-1])  # Accessing the last item
print(fruit_list[::-1])  # Accessing the list in reverse order
print(fruit_list[1:4])  # Accessing a slice of the list

#Updating a list
fruit_list[1] = "Blueberry"  # Changing the second item
fruit_list.append("Grapes")  # Adding a new item
print(fruit_list)

#Adding multiple items
fruit_list.extend(["Kiwi", "Pineapple", "Mango"])
print(fruit_list)

#Removing items
fruit_list.remove("Mango")
print(fruit_list)


"""
List Method Table

| Method                    | Description                                               |
|---------------------------|-----------------------------------------------------      |
| append(item)              | Adds an item to the end of the list.                      |
| extend(iterable)          | Adds multiple items from an iterable to the list.         |
| insert(index, item)       | Inserts an item at a specified index.                     |      
| remove(item)              | Removes the first occurrence of an matching item.                  |
| pop(index)                | Removes and returns the item at the specified index.      |
| clear()                   | Removes all items from the list.                          |
| index(item)               | Returns the index of the first occurrence of an item.     |
| count(item)               | Returns the number of occurrences of an item.             |
| sort()                    | Sorts the items of the list in place.                     |
| sort(reverse=True)       | Sorts the items of the list in place in descending order.  |
| copy()                    | Returns a shallow copy of the list.                       |
| reverse()                 | Reverses the order of the items in the list.              |

"""