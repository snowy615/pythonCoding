"""
ID: yansnow2
LANG: PYTHON3
TASK: milk2
"""
fin = open("milk2.in", "r")
fout = open("milk2.out", "w")
N = int(fin.readline())
start = []
end = []
for i in range(N):
    l = fin.readline().strip("\n")
    l = list(l.split(" "))
    start.append(int(l[0]))
    end.append(int(l[1]))
late = max(end)
num = []
for i in range(late):
    num.append(0)
for i in range(len(start)):
    for j in range(start[i]-1, end[i]-1):
        num[j] = 1
count_one = 0
one = 0
count_zero = 0
zero = 0
print(num)
for i in range(len(num)):
    if num[i] == 0 and max(end)-2 >= i > min(start):
        count_zero += 1
        count_one = 0
    if num[i] == 1:
        count_zero = 0
        count_one += 1
    if count_one > one:
        one = count_one
    if count_zero > zero:
        zero = count_zero
    print(i, count_one, count_zero)
fout.write(f"{one} {zero}\n")
