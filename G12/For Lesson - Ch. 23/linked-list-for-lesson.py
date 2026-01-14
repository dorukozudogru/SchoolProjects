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

def create_new_node(head, number):
    current_node = head
    prev_node = None
    
    nn = Node()
    nn.data = number

    while nn.data > current_node.data:
        prev_node = current_node
        current_node = current_node.pointer

    nn.pointer = current_node
    prev_node.pointer = nn
    
def find_the_target_number(head, target):
    current_node = head
    while current_node.data != target:
        current_node = current_node.pointer
        if current_node.data == target:
            return True
        elif current_node.pointer == None:
            return False

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

number_user = int(input("Enter a number to insert into the linked list: "))
create_new_node(head, number_user)

print_the_linked_list(head)

targeted_number = int(input("Enter a number to search in the linked list: "))
isFound = find_the_target_number(head, targeted_number)
if isFound:
    print(f"The number {targeted_number} is found in the linked list.")
else:
    print(f"The number {targeted_number} is NOT found in the linked list.")