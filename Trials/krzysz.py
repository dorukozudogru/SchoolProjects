DataArray = ["" for i in range(14)]
DataArray = [0, 3, 4, 56, 67, 44, 43, 32, 31, 345, 45, 6, 54, 1]

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def outputArray(array):
    for i in array:
        print(str(i) + " ", end="")
    print("\n")


outputArray(DataArray)
outputArray(insertionSort(DataArray))

def Search(ItemToFind, array):
    for i in range(len(array)):
        if array[i] == ItemToFind:
            return i
    return -1

sortedData = insertionSort(DataArray)
itemsToSearch = [0, 345, 67, 2]
for i in itemsToSearch:
    x = Search(i, sortedData)
    if x != -1:
        print("number " + str(i) + " was found at index " + str(x))
    else:
        print("number " + str(i) + " wasnt found in the list")