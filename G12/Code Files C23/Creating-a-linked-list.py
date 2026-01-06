class Node:
    def __init__(self):
        self.data = None
        self.pointer = None

# Create a linked list with 5 nodes
head = Node()
current_node = head

for i in range(4):
    new_node = Node()
    current_node.data = i * 2
    current_node.pointer = new_node
    current_node = new_node
    

# Set data for the last node
current_node.data = 8
current_node.pointer = None

# Print the linked list
current_node = head
while current_node is not None:
    print(current_node.data, end=" -> ")
    current_node = current_node.pointer