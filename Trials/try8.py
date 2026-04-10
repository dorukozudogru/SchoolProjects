import random

array = []

for x in range(20):
    Value = random.randint(1, 100)
    print(Value)
    array.append(Value)





def PrintArray(arr):
    Counter = 0
    for x in arr:
        print(array[Counter], end=" ")
        Counter = Counter + 1

PrintArray(array)
