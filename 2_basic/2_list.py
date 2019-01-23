
# Simple List
mylist = [1, 2, 4, 5, 6]

# List of strings
mylist_str = ["a", "b", "c"]

# Mixed items List
mixed_list = [1, 3, 5, "hello", "world", 5.5, 7.8, False]

# print list items
print(mixed_list)

# Access list items
print(mixed_list[1])

# Add items to list
mixed_list.append("India")

# Remove items by value
mixed_list.remove("World")
print(mixed_list)

# Remove items by index
del(mixed_list[2])

# convert to a set
dup_list = ["a", "b", "a", "c", "c", "d"]
set(dup_list)
