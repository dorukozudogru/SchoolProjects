def find_node(root, value):
    current = root

    while current is not None:
        if current.data == value:
            return current
        elif value < current.data:
            current = current.left
        else:
            current = current.right
    
    return None

# Assuming binary_tree_root is the root of the binary tree (previous example)
value_to_find = 'H'
found_node = find_node(binary_tree_root, value_to_find)

if found_node is not None:
    print(f"Node with value {value_to_find} found.")
else:
    print(f"Node with value {value_to_find} not found.")
