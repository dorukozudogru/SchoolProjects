my_list = ["a", "z", "f", "f", "b"]

# Convert list to set to remove duplicates
unique_items_set = set(my_list)

# Convert set back to list (if needed)
unique_list = list(unique_items_set)

print("Original List:", my_list)
print("Set:", unique_items_set)
print("List after removing duplicates:", unique_list)
print("second data in the list: ", unique_list[1])