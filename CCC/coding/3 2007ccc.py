# 100,500,1000,5000,10000,25000,50000,100000,500000,1000000
num = int(input())
l = []
t = 0
for a in range(num):
    case = int(input())
    if case == 1:
        l.append(100)
        t += 100
    elif case == 2:
        l.append(500)
        t += 500
    elif case == 3:
        l.append(1000)
        t += 1000
    elif case == 4:
        l.append(5000)
        t += 5000
    elif case == 5:
        l.append(10000)
        t += 10000
    elif case == 6:
        l.append(25000)
        t += 25000
    elif case == 7:
        l.append(50000)
        t += 50000
    elif case == 8:
        l.append(100000)
        t += 100000
    elif case == 9:
        l.append(500000)
        t += 500000
    elif case == 10:
        l.append(1000000)
        t += 1000000
price = int(input())
moneyleft = 100+500+1000+5000+10000+25000+50000+100000+500000+1000000-t
# print(l)
# print(moneyleft)
moneyleft = moneyleft/(10-num)
# print(moneyleft)
if price > moneyleft:
    print('deal')
else:
    print('no deal')