# matrix = [[0,0],[0,0]]


# matrix[0][0] = int(input())
# matrix[0][1] = int(input())
# matrix[1][0] = int(input())
# matrix[1][1] = int(input())


# print(matrix[0][0], matrix[0][1])
# print(matrix[1][0], matrix[1][1])

# arr1d = [0] * 4

# for count in range(4):
#     arr1d[count] = int(input("Please enter a number: "))

# print(arr1d)

arr2d = [[0 for i in range(2)] for j in range(2)]

for row in range(2):
    for column in range(2):
        arr2d[row][column] = int(input("Please enter a number: "))
        
print(arr2d)