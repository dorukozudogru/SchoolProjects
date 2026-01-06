array = [0] * 5
total = 0

for i in range (5):
    array[i] = int(input("Please enter a number: "))
    total = total + array[i]

for i in range(5):
    for j in range(4):
        if array[j] > array[j+1]:
            temp  = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

print("The smallaest number in array is:", array[0])
print("The biggest number in array is:", array[4])
print("The average of the numbers is:", total/5)
