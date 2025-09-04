num = list(map(int, input().split()))
n = num[0]
num.pop(0)
f_lis = []
index = 0
increasing = True
for i in range(n, 0, -1):
    temp_lis = []
    for j in range(i):
        temp_lis.append(num[index])
        index += 1
        index %= len(num)
    print(temp_lis)
    if increasing == False:
        temp_lis.sort(reverse=True)
        increasing = True
    else:
        temp_lis.sort()
        increasing = False
    for j in temp_lis:
        f_lis.append(j)
    if i == 1:
        temp_lis = []
        while (index < len(num) and index > 0):
            temp_lis.append(num[index])
            index += 1
        temp_lis.sort(reverse=not increasing)
        for j in temp_lis:
            f_lis.append(j)
print("--------------")
print(f_lis)
