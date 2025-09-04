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
        if lis.count(0) + 1 == n or min(lis) < 0:
            print(-1)
            break
        max_num = max(lis)
        num_index = lis.index(max_num)
        if num_index == n-1:
            lis[num_index - 1] -= 1
        elif num_index == 0:
            lis[num_index+1] -= 1
        else:
            if lis[num_index-1] > lis[num_index+1]:
                lis[num_index-1] -= 1
            else:
                lis[num_index+1] -= 1
        count += 2
        lis[num_index] -= 1
    if same(lis) == True:
        print(count)