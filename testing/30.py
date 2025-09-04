n = int(input())
for x in range(n):
    a = list(input())
    b = list(input())
    c = list(input())
    if b<c:
        tmp = c
        c = b
        b = tmp
    if a<b:
        tmp = b
        b = a
        a = tmp
    if c == b[:len(c)] or c == b[len(b)-len(c):] or c == a[:len(c)] or c == a[len(a)-len(c):] or b == a[:len(b)] or b == a[len(a)-len(b):]:
        print("No")
    else:
        print("Yes")