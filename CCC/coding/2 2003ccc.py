import math
l = []
inp = 1
times = 0
while True:
    inp = int(input())
    times += 1
    if inp == 0:
        break
    # if inp == 1:
    #     l.append(1)
    #     l.append(1)
    for z in range(int(math.sqrt(inp)), inp+1):
        if inp % z == 0:
            l.append(z)
            l.append(int(inp/z))
            break
# print(l)
for y in range(0, (times-1)*2, 2):
    p = (l[y] + l[y+1]) * 2
    print('Minimum perimeter is %s with dimensions %s x %s' %(p, l[y], l[y+1]))