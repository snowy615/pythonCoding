direction_x = [1, 0, 1, 0, -1, 0, -1, 0, -1, 0, 1, 0]
direction_y = [0, -1, 0, -1, 0, -1, 0, 1, 0, 1, 0, 1]
grid = []
width = int(input())
height = int(input())
c_width = int(input())
c_height = int(input())
for i in range(1, c_width+1):
    for j in range(1, c_height):
        grid.append([i,j])
