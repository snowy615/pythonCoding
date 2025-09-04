n = int(input())
i_temp = list(map(int, input().split()))
t_temp = list(map(int, input().split()))
lis = []
for i in range(n):
    lis.append(i_temp[i]-t_temp[i])
up_max = max(lis)
