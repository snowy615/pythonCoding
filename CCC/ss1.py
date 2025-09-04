a, b, x, y = map(int, input().split())
s1 = (max(x, a) + b+y)*2
s2 = (max(y, b) + a+x)*2
print(min(s1, s2))