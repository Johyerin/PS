#1018 - 체스판 다시 칠하기(silver 4)

import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for i in range(n):
    input = sys.stdin.readline().strip()
    board.append(list(input))

count = 0
list = []
min = 1250
for i in range(n - 7):
    for j in range(m - 7):
        for k in range(7):
            for h in range(7):
                if board[i + k][j + h] == board[i + k][j + h + 1]:
                    count += 1
            if board[i + k][j + h] == board[i + k + 1][j + h]:
                count += 1
        if min > count:
            min = count
            row, col = i, j
        count = 0

change = 0
for i in range(row, row + 7):
    for j in range(col, col + 7):
        if board[i][j] == "B":
            if board[i][j + 1] == "B":
                board[i][j + 1] = "W"
                change += 1

            if board[i + 1][j] == "B":
                board[i + 1][j] = "W"
                change += 1

        elif board[i][j] == "W":
            if board[i][j + 1] == "W":
                board[i][j + 1] = "B"
                change += 1

            if board[i + 1][j] == "W":
                board[i + 1][j] = "B"
                change += 1
print(change)