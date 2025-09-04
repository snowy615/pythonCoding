total = 1
l = []
for z in range(100):
    steps = int(input())
    if steps == 0:
        l.append('You Quit!')
        break
    elif total + steps <= 100:
        total += steps
    if total == 54:
        total = 19
    elif total == 90:
        total = 48
    elif total == 99:
        total = 77
    elif total == 9:
        total = 34
    elif total == 40:
        total = 64
    elif total == 67:
        total = 86
    l.append(total)
    if total == 100:
        l.append('You Win!')
        break
# for y in range(len(l)-1):
#     print('You are now on square %s'%l[y])
if l[-1] == 'You Win!':
    for y in range(len(l) - 1):
        print('You are now on square %s' % l[y])
    print('You Win!')
else:
    for y in range(len(l) - 1):
        print('You are now on square %s' % l[y])
    print(l[-1])