grid = [[0 for i in range(5)] for j in range(8)]
grid[0][1] = 1
def print_grid():
    for row in grid:
        # Use formatted strings to ensure each element takes exactly 4 spaces
        print(''.join(f"{item:7}" for item in row))
def fillGrid(power):
    cnt = 0
    for y in range(8):
        for x in range(5):
            if grid[y][x] == 0:
                grid[y][x] = 2**(power-cnt)
                cnt += 1
                cnt %= 8
fillGrid(9)
print_grid()