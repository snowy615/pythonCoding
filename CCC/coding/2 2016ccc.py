a = input()
b = input()
c = input()
d = input()
l = []
l2 = []
a = a.split()
for u in range(4):
    a[u]=int(a[u])
l.append(a)
b = b.split()
for v in range(4):
    b[v]=int(b[v])
l.append(b)
c = c.split()
for w in range(4):
    c[w]=int(c[w])
l.append(c)
d = d.split()
for x in range(4):
    d[x]=int(d[x])
l.append(d)
for z in range(4):
    for y in range(4):
        l2.append(int(l[z][y]))
if sum(a) == sum(b) and sum(a) == sum(c) and sum(a) == sum(d):
    if sum(b) == sum(c) and sum(b) == sum(d):
        if sum(c) == sum(d):
            if l2[0]+l2[4]+l2[8]+l2[12] == l2[1]+l2[5]+l2[9]+l2[13] and l2[0]+l2[4]+l2[8]+l2[12] == l2[2]+l2[6]+l2[10]+l2[14]:
                if l2[0]+l2[4]+l2[8]+l2[12] == l2[3]+l2[7]+l2[11]+l2[15] and l2[1]+l2[5]+l2[9]+l2[13] == l2[2]+l2[6]+l2[10]+l2[14]:
                    if l2[1]+l2[5]+l2[9]+l2[13] == l2[3]+l2[7]+l2[11]+l2[15] and l2[2]+l2[6]+l2[10]+l2[14] == l2[3]+l2[7]+l2[11]+l2[15]:
                        print('magic')
                    else:
                        print('not magic')
                else:
                    print('not magic')
            else:
                print('not magic')
        else:
            print('not magic')
    else:
        print('not magic')
else:
    print('not magic')