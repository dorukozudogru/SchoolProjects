board = [[0 for i in range(7)] for j in range(6)]

for row in range(1, 6):
    for column in range(1, 7):
        print(board[row][column], end = "")