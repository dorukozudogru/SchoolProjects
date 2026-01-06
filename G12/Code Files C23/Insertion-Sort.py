my_list = [3, 5, 2, 8, 9, 1]

for i in range(1, len(my_list)):
    key = my_list[i]
    j = i - 1
    while j >= 0 and key < my_list[j]:
        my_list[j + 1] = my_list[j]
        j -= 1
        # print("After swapping: ", my_list)
    my_list[j + 1] = key
    # print("After entering the key: ", my_list)
    

print("Sorted array:", my_list)
