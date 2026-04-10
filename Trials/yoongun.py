## 18/26

Queue = [-1]*50
HeadPointer = -1
TailPointer = -1
Queue

def Enqueue(testparameter):
    global Queue, HeadPointer, TailPointer
    if Queue[TailPointer] == 49:
        return False
    else:
        TailPointer += 1
        Queue[TailPointer] = testparameter
        return True

def Dequeue():
    global Queue, HeadPointer, TailPointer
    if Queue[HeadPointer+1] != [-1]:
        ReturningValue = Queue[HeadPointer+1]
        for i in range(TailPointer):
            TempValue = Queue[i+1]
            Queue[i] = TempValue
        Queue[TailPointer] = -1
        TailPointer -= 1
        return ReturningValue

def CreateQueue():
    global Queue, HeadPointer, TailPointer
    File = open("QueueData.txt","r")
    try:
        for line in File:
            if Enqueue(line.strip()) == False:
                print("queue is full")
        File.close()
    except:
        File.close()



CreateQueue()
print(Queue)
Dequeue()
Dequeue()
print(Queue)