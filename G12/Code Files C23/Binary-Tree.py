class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_node(root, value):
    if root is None:
        return Node(value)
    
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
    
    return root

# Example usage:
binary_tree_root = Node('G')

# Adding 6 nodes to the tree in a balanced manner
values_to_add = ['D', 'J', 'B', 'F', 'H', 'L']
for value in values_to_add:
    binary_tree_root = add_node(binary_tree_root, value)
