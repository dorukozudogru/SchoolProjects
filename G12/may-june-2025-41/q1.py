queue = [-1] * 20
headPointer = -1
tailPointer = -1
numberItems = 0

def Enqueue(number):
    global queue, headPointer, tailPointer, numberItems
    if numberItems == 20:
        return False
    else:
        tailPointer += 1
        queue[tailPointer] = number
        numberItems += 1
        return True

def Dequeue():
    global queue, headPointer, tailPointer, numberItems
    if numberItems == 0:
        return False
    else:
        nextItem = queue[headPointer + 1]
        queue[headPointer + 1] = -1
        headPointer += 1
        numberItems -= 1
        return nextItem

for count in range(1, 26):
    isEnqueued = Enqueue(count)
    if isEnqueued:
        print(count, " - Successful")
    else:
        print(count, " - Unsuccessful")

print("After enqueueing action, the updated queue is: ", queue)
        
for count in range(2):
    numberDequeued = -999
    numberDequeued = Dequeue()
    if numberDequeued != False:
        print(numberDequeued, " has been dequeued!")
    else:
        print("Something is wrong!")
        
print("After dequeueing action, the updated queue is: ", queue)