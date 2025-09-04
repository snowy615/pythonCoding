n = []
a = int(input())
for i in range(1, a+1):
    if a % i == 0:
        n.append(i)
print(n)
print(len(n))