# Creating a Node as an object
class Node:
    def __init__(self):
        self.data = None
        self.pointer = None
        
# Printing the linked list
def print_the_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.data, end=" -> ")
        current_node = current_node.pointer
        if current_node == None:
            print("None")
    print()

# _______ MAIN _______
# Create the first node  
head = Node()
current_node = head

# Create other 4 nodes on linked list
for i in range(4):
    new_node = Node()
    current_node.data = i*2
    current_node.pointer = new_node
    current_node = new_node

current_node.data = 8
current_node.pointer = None

# Calling the PROCEDURE for printing the LL
print_the_linked_list(head)