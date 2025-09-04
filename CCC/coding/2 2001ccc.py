m = int(input())
n = int(input())
a = 0
for z in range(100):
    sum = z*m
    if sum % n == 1:
        print(z)
        a += 1
        break
if a == 0:
    print('No such integer exists.')
