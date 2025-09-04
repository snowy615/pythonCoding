a = int(input())
b = []
c: int = 1
while c <= a:
    str = c * '*' + 2 * (a-c) * ' ' + c * '*'
    b.append(str)
    print(str)
    c += 2
b.reverse()
for z in range(1, int(a/2 + 1)):
    print(b[z])