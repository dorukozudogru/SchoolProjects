from collections import deque

stack = deque()
stack.append(10)
stack.append(15)
stack.append(20)
stack.append(25)

print(stack)
print()
print(stack.pop())
print()
print(stack)