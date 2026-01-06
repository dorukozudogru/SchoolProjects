# Creating a Node as an object
class Node:
    def __init__(self):
        self.data = None
        self.pointer = None

# Inserting a new node into an ordered linked list
def insert_a_new_node_into_an_ordered_ll(head, data):
    temp_node = head
    prev_node = None
    
    nn = Node()
    nn.data = data

    while nn.data > temp_node.data:
        prev_node = temp_node
        temp_node = temp_node.pointer

    nn.pointer = temp_node
    prev_node.pointer = nn

# Printing the linked list
def print_the_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.data, end=" -> ")
        current_node = current_node.pointer
        if current_node == None:
            print("None")
    print()
    

def find_the_number_in_the_ll(head, target):
    current_node = head
    while current_node.data != target and current_node.pointer != None:
        current_node = current_node.pointer
        if current_node.data == target:
            return True
        elif current_node.pointer == None:
            return False

def delete_node(head, target):
    isFound = find_the_number_in_the_ll(head, target)
    prev_node = None
    current_node = head
    
    if isFound:
        while current_node.data != target:
            prev_node = current_node
            current_node = current_node.pointer
        if current_node.data == target:
            prev_node.pointer = current_node.pointer
            del current_node
            print("Targeted number has been deleted!\n")
    else:
        print("Targeted number hasn't been found!\n")
    print_the_linked_list(head)

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

# Taking the number from the user to add into the linked list
number = int(input("Please enter a number to add into the linked list: "))

# Calling the PROCEDURE for inserting the number into the LL
insert_a_new_node_into_an_ordered_ll(head, number)

# Calling the PROCEDURE for printing the LL
print_the_linked_list(head)

# Taking the number from the user and calling the FUNCTION
number = int(input("Please enter a number to find: "))
isFound = find_the_number_in_the_ll(head, number)
if isFound:
    print("Targeted number (", number , ") has been found in the linked list.\n")
else:
    print("Targeted number hasn't been found!\n")
    
number = int(input("Please enter a number to delete: "))
delete_node(head, number)