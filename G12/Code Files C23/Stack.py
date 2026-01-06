# Initialize stack variables
base_of_stack = 0 
top_of_stack = -1 
max_stack_size = 5

my_stack = [None] * max_stack_size

def push(newItem):
    global top_of_stack, my_stack  # Declare these variables as global
    if top_of_stack < max_stack_size - 1: 
        top_of_stack += 1
        my_stack[top_of_stack] = newItem

def pop():
    global top_of_stack, my_stack  # Declare these variables as global
    if top_of_stack > -1: 
        item = my_stack[top_of_stack]
        top_of_stack -= 1
        return item

# Example usage
push("A")
push("Z")
push("C")

print(pop())  # Output: C
print(pop())  # Output: Z
print(pop())  # Output: A
