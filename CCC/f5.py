grid_size = int(input())
tree_num = int(input())
x = []
y = []
for i in range(tree_num):
    coordinate = list(map(int, input().split()))
    x.append(coordinate[0])
    y.append(coordinate[1])
area_a = min((x[0]-1),(y[0]-1))
area_b = min((x[0]-1),(grid_size-y[0]))
area_c = min((grid_size-x[0]),(y[0]-1))
area_d = min((grid_size-x[0]),(grid_size-y[0]))
#print(area_d, area_c, area_b, area_a)
print(max(max(area_d, area_c), max(area_b, area_a)))