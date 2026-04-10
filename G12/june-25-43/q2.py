DataArray = [0,3,4,56,67,44,43,32,31,345,45,6,54,1]

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while key < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def OutputArray(arr):
    for item in arr:
        print(item, end=' ')
    print()

def Search(DataArray, ItemToFind):
    low = 0
    high = len(DataArray) - 1
    
    while low <= high:
        mid = (low+high) // 2
        if DataArray[mid] == ItemToFind:
            return mid
        if DataArray[mid] < ItemToFind:
            low = mid + 1
        else:
            high = mid - 1
    return -1

OutputArray(DataArray)
InsertionSort(DataArray)
OutputArray(DataArray)

SearchArray = [0, 345, 67, 2]
for i in range(len(SearchArray)):
    result = Search(DataArray, SearchArray[i])
    if result != -1:
        print(f"Found {SearchArray[i]} at index {result}")
    else:
        print(f"Could not find {SearchArray[i]}")