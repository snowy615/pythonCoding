n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
a = l[0][0]
b = l[0][n-1]
c = l[n-1][0]
d = l[n-1][n-1]
m = min(a, b, c, d)
if m == a:
    print("a")
    for i in range(n):
        for j in range(n):
            print(l[i][j], end=" ")
        print()
elif m == b:
    print("b")
    for i in range(n-1, -1, -1):
        for j in range(n):
            print(l[i][j], end=" ")
        print()
elif m == c:
    print("c")
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(l[i][j], end=" ")
        print()
else:
    print("d")
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            print(l[i][j], end=" ")
        print()