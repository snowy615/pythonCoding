a = int(input())
b = int(input())
c = int(input())
if a < b:
    if a < c:
        if b < c:
            print(b)
        elif b > c:
            print(c)
    elif a > c:
        print(a)
elif a > b:
    if b > c:
        print(b)
    elif b < c:
        if a < c:
            print(a)
        elif a > c:
            print(c)