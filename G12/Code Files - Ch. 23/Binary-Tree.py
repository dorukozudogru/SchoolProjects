class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_node(root, value):
    current = root
    while True:
        if value < current.data:
            if current.left is not None:
                current = current.left
            else:
                current.left = Node(value)
                break
        else:  # value >= current.data
            if current.right is not None:
                current = current.right
            else:
                current.right = Node(value)
                break

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
        
def print_tree_structure(node, level=0):
    if node is not None:
        print_tree_structure(node.right, level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree_structure(node.left, level + 1)

# Example usage:
binary_tree_root = input("Enter the root value of the binary tree: ").upper()
binary_tree_root = Node(binary_tree_root)

# Adding 6 nodes to the tree in a balanced manner
values_to_add = ['D', 'E', 'J', 'B', 'F', 'H', 'L']
for value in values_to_add:
    add_node(binary_tree_root, value)

print("\nBinary tree structure:")
print_tree_structure(binary_tree_root)

value_to_find = input("\nEnter a value to find in the binary tree: ").upper()
found_node = find_node(binary_tree_root, value_to_find)

if found_node is not None:
    print(f"Node with value {value_to_find} found.")
else:
    print(f"Node with value {value_to_find} not found.")
