arr = [32, 12, 45, 78, 99, 0, 1]

for i in range(6):
    for j in range(6):
        if (arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)