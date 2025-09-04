l = []
for z in range(100000):
    num = int(input())
    if num == 99999:
        break
    d1 = int(num/10000)
    d2 = int(num/1000)-int(num/10000)*10
    d = d1 + d2
    if d == 0:
        l.append(rl)
    elif d % 2 == 0:
        rl = 'right'
        l.append('right')
    else:
        rl = 'left'
        l.append('left')
    fn = num - int(num/1000)*1000
    l.append(fn)
# fin = int(len(l)/2)
# print(l)
for y in range(0, len(l), 2):
    print('%s %s'%(l[y], l[y+1]))