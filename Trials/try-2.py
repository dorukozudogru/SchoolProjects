class ListNode(object):
    def __init__(self, data=0):
        self.data = data
        self.pointer = None

finalNode = ListNode()

def print_the_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.data, end=" -> ")
        current_node = current_node.pointer
        if current_node == None:
            print("None")
    print()

def createFinalNode(head, data):
    global finalNode
    if finalNode is None:
        finalNode = ListNode(data)
        return finalNode
    current = finalNode
    while current.pointer is not None:
        current = current.pointer
    current.pointer = ListNode(data)
    return finalNode

def calculate(l1, l2):
    global finalNode
    current1 = l1
    current2 = l2
    carry = 0

    while l1 != None and l2 != None:
        sum = l1.data + l2.data + carry
        carry = sum // 10
        if carry > 0:
            sum = sum % 10
        
        l1 = l1.pointer
        l2 = l2.pointer
        
        create_new_node(finalNode, sum)
        
        print_the_linked_list(finalNode)

def create_new_node(head, number):
    if head is None or head.data == 0:
        nn = ListNode()
        nn.data = number
        nn.pointer = None
        head = nn
        return head

    current = head
    while current.pointer is not None:
        current = current.pointer

    nn = ListNode()
    nn.data = number
    nn.pointer = None
    current.pointer = nn

    return head

headFirst = ListNode()
headSecond = ListNode()
numberFirstNode = 0
numberSecondNode = 0

while numberFirstNode != -1:
    numberFirstNode = int(input("Enter a number to insert into the FIRST linked list (-1 to stop): "))
    if numberFirstNode != -1:
        headFirst = create_new_node(headFirst, numberFirstNode)

print_the_linked_list(headFirst)

while numberSecondNode != -1:
    numberSecondNode = int(input("Enter a number to insert into the SECOND linked list (-1 to stop): "))
    if numberSecondNode != -1:
        headSecond = create_new_node(headSecond, numberSecondNode)

print_the_linked_list(headSecond)

calculate(headFirst, headSecond)