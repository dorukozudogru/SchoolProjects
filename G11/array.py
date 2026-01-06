#1D Array
studentList = ["Kuba", "Julia"]

#Adding new items to the list
studentList.append("Yoongun")
studentList.append("Atharva")
studentList.append("Krzysztof")

#Print all the list
print(studentList)

#    0        1         2          3           4
# ['Kuba', 'Julia', 'Yoongun', 'Atharva', 'Krzysztof']

#Print only the item in index #2
print(studentList[2])

#2D Array
#             0       1       2         3          4
numbers = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
#           0 1 2   0 1 2   0 1 2    0  1  2    0  1  2

# Print the third element (index 2) of the first list (index 0) in the 'numbers' 2D list
print(numbers[0][2])