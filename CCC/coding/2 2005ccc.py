a = int(input())
b = int(input())
total = 0
for i in range(a, b+1):
    sum = 0
    for z in range(1, i+1):
        if i % z == 0:
            sum += 1
    if sum == 4:
        total += 1
print('The number of RSA numbers between %s and %s is %s' % (a, b, total))