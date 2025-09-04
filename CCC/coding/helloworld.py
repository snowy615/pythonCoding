e = []
d = input()
e = d.split()
a = int(e[0])
b = int(e[1]) + 1
c = 2
print('Sun Mon Tue Wed Thr Fri Sat')
if a == 1:
    print('  1', end='')
    while c < b:
        if c < 10:
            if c % 7 == 1 and c > 1:
                print()
                print('  %s'%(c), end='')
                c+=1
            else:
                print('   %s'%(c), end='')
                c+=1
        else:
            if c % 7 == 1:
                print()
                print(' %s' % (c), end='')
                c+=1
            else:
                print('  %s'%(c), end='')
                c+=1

if a == 2:
    print('      1', end='')
    while c < b:
        if c < 10:
            if c % 7 == 0:
                print()
                print('  %s'%(c), end='')
                c+=1
            else:
                print('   %s'%(c), end='')
                c+=1
        else:
            if c % 7 == 0:
                print()
                print(' %s' % (c), end='')
                c+=1
            else:
                print('  %s'%(c), end='')
                c+=1

if a == 3:
    print('          1', end='')
    while c < b:
        if c < 10:
            if c % 7 == 6:
                print()
                print('  %s'%(c), end='')
                c+=1
            else:
                print('   %s'%(c), end='')
                c+=1
        else:
            if c % 7 == 6:
                print()
                print(' %s' % (c), end='')
                c+=1
            else:
                print('  %s'%(c), end='')
                c+=1

if a == 4:
    print('              1', end='')
    while c < b:
        if c < 10:
            if c % 7 == 5:
                print()
                print('  %s'%(c), end='')
                c+=1
            else:
                print('   %s'%(c), end='')
                c+=1
        else:
            if c % 7 == 5:
                print()
                print(' %s' % (c), end='')
                c+=1
            else:
                print('  %s'%(c), end='')
                c+=1

if a == 5:
    print('                  1', end='')
    while c < b:
        if c < 10:
            if c % 7 == 4:
                print()
                print('  %s'%(c), end='')
                c+=1
            else:
                print('   %s'%(c), end='')
                c+=1
        else:
            if c % 7 == 4:
                print()
                print(' %s' % (c), end='')
                c+=1
            else:
                print('  %s'%(c), end='')
                c+=1

if a == 6:
    print('                      1', end='')
    while c < b:
        if c < 10:
            if c % 7 == 3:
                print()
                print('  %s'%(c), end='')
                c+=1
            else:
                print('   %s'%(c), end='')
                c+=1
        else:
            if c % 7 == 3:
                print()
                print(' %s' % (c), end='')
                c+=1
            else:
                print('  %s'%(c), end='')
                c+=1

if a == 7:
    print('                          1', end='')
    while c < b:
        if c < 10:
            if c % 7 == 2:
                print()
                print('  %s'%(c), end='')
                c+=1
            else:
                print('   %s'%(c), end='')
                c+=1
        else:
            if c % 7 == 2:
                print()
                print(' %s' % (c), end='')
                c+=1
            else:
                print('  %s'%(c), end='')
                c+=1
print('')

