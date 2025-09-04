n = int(input())
for x in range(n):
    a = list(input())
    b = list(input())
    c = list(input())
    print(a[len(a)-n:], b[len(b)-n:], c[len(c)-n:])
    if len(a)<n or len(b)<n or len(c)<n:
        print("No")
    elif a[:n]!=b[:n] and b[:n]!=c[:n] and a[:n]!=c[:n] and a[len(a)-n:] != b[len(b)-n:] != c[len(c)-n:]:
        print("Yes")
    else:
        print("No")