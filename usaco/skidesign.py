"""
ID: yansnow2
LANG: PYTHON3
TASK: skidesign
"""
fin = open("skidesign.in", "r")
fout = open("skidesign.out", "w")
n = int(fin.readline())
l = []
sum = 0
for i in range(n):
    num = int(fin.readline())
    sum += num
    l.append(num)
sum /= n
int(sum)
print(sum)
total = 0
for i in range(len(l)):
    if sum - 8.5 < l[i] < sum + 8.5:
        pass
    else:
        print((abs(l[i]-(sum+9)))**2)
        total += (abs(l[i]-(sum+9)))**2
print(total)