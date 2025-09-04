l = []
d = []
for z in range(100):
    ins = input()
    if ins == 'SCHOOL':
        break
    elif ins == 'L':
        d.append('RIGHT')
    elif ins == 'R':
        d.append('LEFT')
    else:
        l.append(ins)
l.reverse()
l.append('HOME')
d.reverse()
# print(l)
for y in range(len(l)-1):
    print("Turn %s onto %s street." %(d[y], l[y]))
print('Turn %s into your %s.'%(d[-1], l[-1]))