def same(lis):
    if lis.count(lis[0]) == len(lis):
        return True
    else:
        return False

t = int(input())
for x in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    count = 0
    if same(lis) == True:
        print(0)
        continue
    while same(lis) == False:
        #print(f"lis{lis}")
        min_num = min(lis)
        if lis.count(0) + 1 == len(lis) or min(lis) < 0:
            print(-1)
            break
        for i in range(len(lis)-1):
            two_min = min(lis[i], lis[i+1])
            if two_min >= min_num:
                count += 2
                lis[i] -= 1
                lis[i+1] -= 1
    if same(lis) == True:
        print(count)
        continue
