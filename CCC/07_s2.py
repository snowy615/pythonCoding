n = int(input())
size = []
for i in range(n):
    lis = list(map(int, input().split()))
    lis.sort()
    lis.insert(0, lis[0]*lis[1]*lis[2])
    size.append(lis)
size.sort()
m = int(input())
#print(size)
for i in range(m):
    lis = list(map(int, input().split()))
    min_num = 1000000010
    lis.sort()
    for j in range(n):
        #print(size[j][1], lis[0], size[j][2], lis[1], size[j][3],lis[2])
        if size[j][1]>=lis[0] and size[j][2]>=lis[1] and size[j][3]>=lis[2]:
            min_num = min(min_num, size[j][0])
    if min_num == 1000000010:
        print("Item does not fit.")
    else:
        print(min_num)
