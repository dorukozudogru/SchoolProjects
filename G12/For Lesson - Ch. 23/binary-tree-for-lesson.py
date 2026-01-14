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
        elif value > current.data:
            if current.right is not None:
                current = current.right
            else:
                current.right = Node(value)
                break
        else:
            break  # value already exists in the tree
        
def find_node(root, letter):
    current = root
    
    while current is not None:
        if current.data == letter:
            return True
        if letter < current.data:
            current = current.left
        elif letter > current.data:
            current = current.right
    
        
def print_tree_structure(node, level=0):
    if node is not None:
        print_tree_structure(node.right, level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree_structure(node.left, level + 1)
        
root = input("Enter the root node value: ")
root = Node(root)
items_to_be_added = ["P","T","D","A","H","E","L", "H", "L"]
for item in items_to_be_added:
    add_node(root, item)
    
print_tree_structure(root)

target_value = input("Enter a value to search in the binary tree: ")

returned_find_node = False
returned_find_node = find_node(root, target_value)
if returned_find_node:
    print(f"Node with value {target_value} found.")
else:
    print(f"Node with value {target_value} not found.")