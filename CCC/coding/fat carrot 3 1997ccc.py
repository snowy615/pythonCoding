n = int(input())
for i in range(n):
    number1 = int(input())
    number2 = int(input())
    number3 = int(input())
    a = []
    b = []
    c = []
    for u in range(number1):
        a.append(input())
    for v in range(number2):
        b.append(input())
    for w in range(number3):
        c.append(input())
    for u in range(number1):
        for v in range(number2):
            for w in range(number3):
                print("%s %s %s."%(a[u],b[v],c[w]))
