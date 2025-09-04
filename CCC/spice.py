n = int(input())
lis = []
for i in range(n):
    name, m, rating, color = input().split()
    c = 10
    if color == "White":
        c = 0
    elif color == "Red":
        c = 1
    elif color == "Brown":
        c = 2
    elif color == "Orange":
        c = 3
    elif color == "Blue":
        c = 4
    lis.append([5-int(rating), c, 100-int(m), name])
lis.sort()
x = 0
for i in range(n):
    print(lis[i][3])