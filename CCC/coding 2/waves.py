num = list(map(int, input().split()))
n = num[0]
num.pop(0)
f_lis = []
l_index = 0
r_index = 0
increasing = True
for i in range(n, 0, -1):
    l_index = r_index
    r_index += i
    l_index %= len(num)
    r_index %= len(num)
    if r_index>l_index:
        temp_lis = num[l_index:r_index]
    else:
        temp_lis = num[l_index:]+num[:r_index]
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
        if r_index != 0:
            temp_lis = num[r_index:]
            temp_lis.sort(reverse=not increasing)
            for j in temp_lis:
                f_lis.append(j)
print("--------------")
print(f_lis)
