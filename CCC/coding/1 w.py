n = int(input())
d=[]
for i in range(n):
    a = input()
    b = []
    b = a.split()
    P = float(b[0])
    C = float(b[1])
    o = 100*P/(100+C)
    d.append(o)
for z in range(n):
    print(d[z])