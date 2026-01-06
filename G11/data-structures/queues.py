from collections import deque

queue = deque()
queue.append(10)
queue.append(15)
queue.append(20)
queue.append(25)

print(queue)
print()
print(queue.popleft())
print()
print(queue)