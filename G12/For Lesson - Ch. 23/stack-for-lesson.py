base_of_stack = 0
top_of_stack = -1
max_size = 5

stack = [None] * max_size

def push_stack(value):
    global top_of_stack, base_of_stack, max_size
    if top_of_stack < max_size - 1:
        top_of_stack += 1
        stack[top_of_stack] = value
        
def pop_stack():
    global top_of_stack, base_of_stack, max_size
    if top_of_stack >= base_of_stack:
        poped_out_value = stack[top_of_stack]
        stack[top_of_stack] = None # Clear the position (depends on the question)
        top_of_stack -= 1
        return poped_out_value
    
push_stack("Y")
push_stack("A")
push_stack("Ku")
push_stack("Krz")
push_stack("D")
push_stack("O")  # This push should not work as the stack is full

print("Popped out value:", pop_stack())

print(stack)