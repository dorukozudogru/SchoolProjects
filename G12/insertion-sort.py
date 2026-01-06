numbers = [9, 12, 7, 10, 2, 13]

for index in range(1, len(numbers)):
    j = index - 1
    key = numbers[index]
    
    while key < numbers[j] and j >= 0:
        numbers[j+1] = numbers[j]
        j -= 1
    numbers[j+1] = key
    
print(numbers)