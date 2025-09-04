import copy
import math

grid = [[0 for i in range(5)] for j in range(8)]
mgrid = copy.deepcopy(grid)
xx = [-1, 0, 1, -1, 0, 1, -1, 0, 1, ]
yy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

maxPath = []

# dfs var
tmp = [] #temp max
path = []
used = [[0 for a in range(5)] for b in range(8)]


# start index row (x), start index column (y)
def tryPath(x, y):
    global tmp
    notMove = True
    for i in range(8):
        a = x + xx[i]
        b = y + yy[i]
        if 0 <= a < 4 and 0 <= b <= 7 and (mgrid[y][x] == mgrid[b][a] or 2 * mgrid[y][x] == mgrid[b][a]):
            print(a, b)
            notMove = False
            used[b][a] = 1
            path.append([a, b])
            tryPath(a, b)
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
    for y in range(8):
        for x in range(5):
            mgrid = copy.deepcopy(grid)
            tmp = [[x, y]]  # temp max
            path = [[x, y]]
            used = [[0 for a in range(5)] for b in range(8)]
            tryPath(x, y)
            if len(tmp) > len(maxPath):
                maxPath = tmp
    #finished path finding

    #sum of path + remove elements in path + update the last value
    pathSum = 0
    for i in range(len(maxPath)):
        pathSum += grid[maxPath[i][1]][maxPath[i][0]]
        if i != len(maxPath)-1:
            grid[maxPath[i][1]][maxPath[i][0]] = 0

    power = math.ceil(math.log2(pathSum))
    maxNumber = 2**power
    grid[maxNumber[-1][1]][maxNumber[-1][0]] = maxNumber

    #so far assuming 8 consecutive numbers total
    minKeep = 2**(power-7)
    removeMin(minKeep)
    #finshed removing numbers

    #transform down
    transformDown()

    #fill grid
    fillGrid(power)

def play2248(boardValues):
    global grid
    gridValues = list(map(int, boardValues.split()))
    for y in range(8):
        for x in range(5):
            grid[y][x] = gridValues[y*5+x]
    subPlay()
    subPlay()
    subPlay()

    result = ""
    for y in range(8):
        for x in range(5):
            result += str(grid[y][x]) + " "
    return result

play2248("4 128 4 128 32 16 16 4 256 16 32 4 16 64 4 8 64 64 256 8 16 2 2 256 4 32 128 2 64 8 256 32 128 16 2 8 32 32 4 32")