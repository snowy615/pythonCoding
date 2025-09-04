a = int(input())
c = []
for i in range(a):
    l = []
    b = input()
    l = b.split()
    c.append(int(l[0])* l[1])
for z in range(a):
    print(c[z])
