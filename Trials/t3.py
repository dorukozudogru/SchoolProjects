import random
RandomArr = ["" for i in range(20)]
for i in range(20):
    while True:
        found = False
        num = random.randrange(0, 100)
        for j in RandomArr:
            if num == j:
                found = True
        if found == False:
            RandomArr[i] = num
            break
        else:
            continue


def PrintArray(Arr):
    string = ""
    for i in Arr:
        string += f"{i} "
    print(string)

def BubbleSort(Arr):
    for i in range(len(Arr)):
        for j in range(len(Arr) - 1):
            if Arr[j] > Arr[j + 1]:
                Arr[j], Arr[j + 1] = Arr[j + 1], Arr[j]
                
                
def RecursiveBinarySearch(Arr, Upper, Lower, Val, jumps = 0):
    Target = round((Upper - Lower)/2)
    TargetVal = Arr[Target + Lower]
    print("target" + str(TargetVal))
    print("upper" + str(Upper))
    print("lower " + str(Lower))
    print("\n")
    if TargetVal == Val:
        print("found " + str(Target+Lower))
        return Target + Lower
    elif Upper == Lower:
        print("notFound")
        return -1
    elif Upper - Lower == 1 or Upper - Lower == -1:
        return -1
    elif TargetVal > Val:
        RecursiveBinarySearch(Arr, Target, Lower, Val, jumps + 1)
    elif TargetVal < Val:
        RecursiveBinarySearch(Arr, Upper, Target + Lower, Val, jumps + 1)


PrintArray(RandomArr)
BubbleSort(RandomArr)
print("Sorted")
PrintArray(RandomArr)

DataToFind = int(input("Enter the number to find "))
Location = RecursiveBinarySearch(RandomArr, 19, 0, DataToFind)
if Location == -1:
    print("Not found")
else:
    print("Found at position", Location)