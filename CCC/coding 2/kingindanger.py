def gridPrint(grid):
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()
    print("------------")
grid = [[0 for i in range(8)] for j in range(8)]
s = input().split()
k_row = 0
k_col = 0
for piece in s:
    row = 8 - int(piece[2])
    col = ord(piece[1])-ord('a')
    grid[row][col] = 2
for piece in s:
    row = 8 - int(piece[2])
    col = ord(piece[1])-ord('a')

    print(piece[0], row, col)
    if piece[0] == "K":
        k_row = row
        k_col = col
        continue
    if piece[0] == "R" or piece[0] == "Q":
        for i in range(4):
            row_direction = [1, 0, -1, 0]
            col_direction = [0, -1, 0, 1]
            temp_row = row
            temp_col = col
            while True:
                temp_row += row_direction[i]
                temp_col += col_direction[i]
                if temp_row < 0 or temp_row > 7 or temp_col < 0 or temp_col > 7:
                    break
                if grid[temp_row][temp_col] == 2 or grid[temp_row][temp_col] == 3 :
                    grid[temp_row][temp_col] = 3
                    break
                grid[temp_row][temp_col] = 1
    if piece[0] == "B" or piece[0] == "Q":
        row_direction = [1, 1, -1, -1]
        col_direction = [1, -1, 1, -1]
        for i in range(4):
            temp_row = row
            temp_col = col
            while True:
                temp_row += row_direction[i]
                temp_col += col_direction[i]
                if temp_row < 0 or temp_row > 7 or temp_col < 0 or temp_col > 7:
                    break
                if grid[temp_row][temp_col] == 2 or grid[temp_row][temp_col] == 3:
                    grid[temp_row][temp_col] = 3
                    break
                grid[temp_row][temp_col] = 1
    if piece[0] == "N":
        # row_direction = [-2, -1, 1, 2, 2, 1, -1, -2]
        # col_direction = [1, 2, 2, 1, -1, -2, -2, -1]
        row_direction = [-2, -2, -1, -1, 1, 1, 2, 2]
        col_direction = [-1, 1, -2, 2, -2, 2, -1, 1]
        for i in range(8):
            temp_row = row
            temp_col = col
            temp_row += row_direction[i]
            temp_col += col_direction[i]
            if temp_row < 0 or temp_row > 7 or temp_col < 0 or temp_col > 7:
                continue
            if grid[temp_row][temp_col] == 2 or grid[temp_row][temp_col] == 3:
                grid[temp_row][temp_col] = 3
                break
            grid[temp_row][temp_col] = 1

    if piece[0] == "P":
        row_direction = [-1, -1]
        col_direction = [-1, 1]
        for i in range(2):
            temp_row = row
            temp_col = col
            temp_row += row_direction[i]
            temp_col += col_direction[i]
            if temp_row < 0 or temp_row > 7 or temp_col < 0 or temp_col > 7:
                continue
            if grid[temp_row][temp_col] == 2 or grid[temp_row][temp_col] == 3:
                grid[temp_row][temp_col] = 3
                break
            grid[temp_row][temp_col] = 1
    gridPrint(grid)

surrounded = True
row_direction = [1, 1, 1, 0, 0, -1, -1, -1]
col_direction = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(8):
    temp_row = k_row
    temp_col = k_col
    temp_row += row_direction[i]
    temp_col += col_direction[i]
    if temp_row < 0 or temp_row > 7 or temp_col < 0 or temp_col > 7:
        continue
    if grid[temp_row][temp_col] == 0 or grid[temp_row][temp_col] == 2:
        surrounded = False
        break
if surrounded == True and (grid[k_row][k_col] == 1 or grid[k_row][k_col] == 3):
    print("CHECKMATE")
if surrounded == True and (grid[k_row][k_col] == 0 or grid[k_row][k_col] == 2):
    print("STALEMATE")
if surrounded == False and (grid[k_row][k_col] == 1 or grid[k_row][k_col] == 3):
    print("CHECK")
if surrounded == False and (grid[k_row][k_col] == 0 or grid[k_row][k_col] == 2):
    print("SAFE")