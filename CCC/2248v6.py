import copy
import math
#passed 2

grid = [[0 for i in range(5)] for j in range(8)]
mgrid = copy.deepcopy(grid)
xx = [-1, 0, 1, -1, 1, -1, 0, 1]
yy = [-1, -1, -1, 0, 0, 1, 1, 1]

maxPath = []

# dfs var
tmp = [] #temp max
path = []
used = [[0 for a in range(5)] for b in range(8)]


def print_grid():
    for row in grid:
        # Use formatted strings to ensure each element takes exactly 4 spaces
        print(''.join(f"{item:7}" for item in row))



# start index row (x), start index column (y)
def tryPath(x, y, ct):
    global tmp
    notMove = True
    for i in range(8):
        a = x + xx[i]
        b = y + yy[i]
        if 0 <= a <= 4 and 0 <= b <= 7 and used[b][a] == 0:
            if (ct < 2 and mgrid[y][x] == mgrid[b][a]) or (ct >= 2 and (mgrid[y][x] == mgrid[b][a] or 2 * mgrid[y][x] == mgrid[b][a])):
                notMove = False
                used[b][a] = 1
                path.append([a, b])
                tryPath(a, b, ct+1)
                used[b][a] = 0
                path.remove([a, b])

    if notMove == True:
        if len(path) > len(tmp):
            tmp = copy.deepcopy(path)
        return


def removeMin(minKeep):
    for y in range(8):
        for x in range(5):
            if grid[y][x] < minKeep:
                grid[y][x] = 0


def inOrder(c):
    for i in range(7, 0, -1):
        if grid[i][c] == 0 and grid[i-1][c] != 0:
            return False
    return True


def down(c):
    for i in range(7, 0, -1):
        if grid[i][c] == 0 and grid[i-1][c] != 0:
            grid[i][c] = grid[i-1][c]
            grid[i-1][c] = 0

def transformDown():
    for c in range(5):
        while True:
            if inOrder(c):
                break
            down(c)


def fillGrid(power):
    cnt = 0
    for y in range(8):
        for x in range(5):
            if grid[y][x] == 0:
                grid[y][x] = 2**(power-cnt)
                cnt += 1
                cnt %= 8



def subPlay():
    global tmp, used, path, grid, mgrid, maxPath
    # find path
    for x in range(5):
        for y in range(8):
            mgrid = copy.deepcopy(grid)
            tmp = [[x, y]]  # temp max
            path = []
            used = [[0 for a in range(5)] for b in range(8)]
            tryPath(x, y, 1)
            if len(tmp) > len(maxPath):
                maxPath = tmp
    #finished path finding
    print("max path")
    print(maxPath)
    #sum of path + remove elements in path + update the last value
    pathSum = 0
    for i in range(len(maxPath)):
        pathSum += grid[maxPath[i][1]][maxPath[i][0]]
        if i != len(maxPath)-1:
            grid[maxPath[i][1]][maxPath[i][0]] = 0

    power = math.ceil(math.log2(pathSum))
    maxNumber = 2**power
    grid[maxPath[-1][1]][maxPath[-1][0]] = maxNumber
    print(f"{maxNumber} maxNumber")
    print("new grid after path finding")
    print_grid()

    #so far assuming 8 consecutive numbers total
    minKeep = 2**(power-7)
    removeMin(minKeep)
    #finshed removing numbers
    print("new grid after removing min")
    print_grid()
    #transform down
    transformDown()
    print("new grid after transforming down")
    print_grid()

    #fill grid
    fillGrid(power)
    print("new grid after filling")
    print_grid()
    print("----------------------------------")

def play2248(boardValues):
    global grid, maxPath
    gridValues = list(map(int, boardValues.split()))
    for x in range(5):
        for y in range(8):
            grid[y][x] = gridValues[y*5+x]
    print_grid()
    maxPath = []
    print("---------------")
    subPlay()
    print_grid()
    maxPath = []
    print("---------------")
    subPlay()
    print(grid)
    print("---------------")
    subPlay()
    maxPath = []
    print_grid()
    print("---------------")

    result = ""
    for y in range(8):
        for x in range(5):
            result += str(grid[y][x]) + " "
    return result

#play2248("4 128 4 128 32 16 16 4 256 16 32 4 16 64 4 8 64 64 256 8 16 2 2 256 4 32 128 2 64 8 256 32 128 16 2 8 32 32 4 32")
#play2248("256 128 64 128 32 32 16 8 256 16 4 2 16 64 4 4 128 64 256 8 16 16 2 256 4 32 64 2 64 8 256 2 128 16 2 8 128 256 4 32")
play2248("256 8 4 16 128 64 4 32 256 256 8 32 8 4 2 64 128 8 2 8 64 16 64 16 128 4 4 4 4 64 64 2 8 8 32 128 128 128 64 4")
print("2048 1024 512 256 128 64 32 16 2048 1024 512 512 256 128 64 32 256 32 16 2048 256 16 1024 512 256 64 2048 128 64 128 64 512 128 16 64 128 128 128 64 32")
#play2248("4 16 8 2 32 2 2 8 32 4 2 16 16 4 128 128 8 4 2 128 128 64 8 128 128 4 2 16 32 16 8 8 128 16 32 32 8 128 2 128")