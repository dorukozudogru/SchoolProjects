import random
Array = [None] * 20
for r in range(0, 20):
    Array[r] = random.random()

def PrintArray(Array):
    for i in range(len(Array)):
        print(Array[i]) 
    

def BubbleSort(Array):
    Temp = None
    for k in range(len(Array)):
        for j in range(1, len(Array)):
            if Array[j-1] > Array[j]:
                Temp = Array[j-1]
                Array[j-1] = Array[j]
                Array[j] = Temp
        
    return Array

def RecursiveBinarySearch(Array, Lower, Upper, Value):
    Found = False
    while Found == False:
        Middle = round((Upper + Lower) / 2)
        if Array[Middle] == Value:
            Found = True
            return Middle
        elif Value > Array[Middle]:
            Lower = Middle
        elif Value < Array[Middle]:
            Upper = Middle
        elif Upper == Lower + 1 or Upper == Lower:
            return -1
            break
        
        

PrintArray(Array)
print("Sorted")
PrintArray(BubbleSort(Array))

value = int(input("enter a number: "))
output = RecursiveBinarySearch(Array, 0, 20, value)
if output == -1:
    print("number not found")
else:
    print("number was found in position: ", output)
    






    
