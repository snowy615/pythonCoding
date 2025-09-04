import copy
def c(row, lis):
    for k in range(l):
        if lis[row][k] == lis[row-1][k]:
            lis[row][k] = 0
        else:
            lis[row][k] = 1
r = int(input())
l = int(input())
or_lis = []
last_row = []
for x in range(r):
    or_lis.append(list(map(int, input().split())))
last_row.append(or_lis[r-1])
for i in range(1, r):
    lis = copy.deepcopy(or_lis)
    for j in range(i, r):
        c(j, lis)
    if lis[r-1] not in last_row:
        last_row.append(lis[r-1])
print(len(last_row))
