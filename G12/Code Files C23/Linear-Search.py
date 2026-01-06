my_list = [3, 5, 2, 8, 9, 1]
target = 9
found = False

for i in range(len(my_list)): 
    if my_list[i] == target:
        found = True
        break

if found: 
    print("Target found")
else: 
    print("Target not found")
