num = int(input())
l = []
x = []
y = []
for z in range(num):
    cord = input()
    l.append(cord.split(','))
    x.append(int(l[z][0]))
    y.append(int(l[z][1]))
smallx = x[0]
smally = y[0]
largex = x[0]
largey = y[0]
for a in range(num):
    if x[a] <= smallx:
        smallx = x[a]
    if x[a] >= largex:
        largex = x[a]
    if y[a] <= smally:
        smally = y[a]
    if y[a] >= largey:
        largey = y[a]
print('%s,%s' %(smallx-1, smally-1))
print('%s,%s' %(largex+1, largey+1))