def p(lis):
    if len(lis) == 0:
        return []
    if len(lis) == 1:
        return [lis]
    l = []
    for i in range(len(lis)):
        m = lis[i]
        remain_lis = lis[:i] + lis[i+1:]
        for j in p(remain_lis):
            l.append([m]+j)
    return l
def check()
lis = [[1,7], [1,4], [2,1], [3,4], [3,5]]
possible_permutation = p([1, 2, 3, 4, 5, 6, 7])
while True:
    x = int(input())
    y = int(input())
    if x == 0 and y == 0:
        break
    lis.append([x,y])
for i in range(len(possible_permutation)):
    ha = possible_permutation[i]
    for j in range(len(lis)):
        if ha.index(lis[j][0]) > ha.index(lis[j][1]):
            break
