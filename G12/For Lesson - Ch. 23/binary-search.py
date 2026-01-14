my_list = [11,12,22,25,34,64,90,100,121,123]
target = int(input("Please enter a target number: "))
found = False

low = 0
high = len(my_list) - 1

while low <= high:
    mid = (low + high) // 2
    if my_list[mid] == target:
        found = True
        break
    elif my_list[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Item found")
else:
    print("Item not found")
