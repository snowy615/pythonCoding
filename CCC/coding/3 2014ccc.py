num = int(input())
a = 100
d = 100
for z in range(num):
    ha = input()
    ha = ha.split()
    if int(ha[0]) > int(ha[1]):
        d = d - int(ha[0])
    elif int(ha[0]) < int(ha[1]):
        a = a - int(ha[1])
    else:
        continue
print(a)
print(d)