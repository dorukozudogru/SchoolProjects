DataArray = [0, 3, 4, 56, 67, 44, 43, 32, 31, 345, 45, 6, 54, 1]

def InsertionSort(DataArray):
    for i in range(1, len(DataArray)):
        if DataArray[i-1] > DataArray[i]:
            DataArray[i-1], DataArray[i] = DataArray[i], DataArray[i-1]
            for j in range(0, i):
                if DataArray[i-j] < DataArray[i-j-1]:
                    DataArray[i-j-1], DataArray[i-j] = DataArray[i-j], DataArray[i-j-1]


def OutputArray(DataArray):
    string = ""
    for i in range(0, len(DataArray)):
        string += str(DataArray[i])
        string += " "
    print(string)

def Search(DataArray, ItemToFind):
    upper = len(DataArray)-1
    lower = 0
    middle = 0
    found = False
    while lower <= upper:
        middle = (lower + upper)//2
        if DataArray[middle] == ItemToFind:
            found = True
            break
        elif DataArray[middle] < ItemToFind:
            lower = middle + 1
        else:
            upper = middle-1
    if found:
        return middle
    else:
        return -1


OutputArray(DataArray)
InsertionSort(DataArray)
OutputArray(DataArray)

foundinglist = [0, 345, 67, 2]
for m in range(0, len(foundinglist)):
    output = Search(DataArray, foundinglist[m])
    if output != -1:
        print("the index for ", foundinglist[m], " is ", output)
    else:
        print("index not found")