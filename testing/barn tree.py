n = int(input())
hay = list(map(int, input().split()))
road = []
sum = 0
for i in range(n-1):
    road.append(list(map(int, input().split())))
    sum += hay[i]
avg = int((sum+hay[n-1])/n)
