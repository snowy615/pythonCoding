n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())

if a == b == c == d:
    print(4)
if a+b == 2*c == 2*d or b+c == 2*a == 2*d or a+c == 2*b == 2*c:
    print(3)
    