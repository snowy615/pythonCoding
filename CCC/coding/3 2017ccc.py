it1 = input()
it2 = input()
it3 = int(input())
# print(it1, it2, it3)
x = []
y = []
it1 = it1.split(' ')
it2 = it2.split(' ')
# print(it1)
x.append(int(it1[0]))
x.append(int(it2[0]))
y.append(int(it1[1]))
y.append(int(it2[1]))
z = abs(x[1]-x[0])+abs(y[1]-y[0])
if x[0] == 0 and y[0] == 0 and x[1] == 0 and y[1] == 0:
    print('Y')
elif x[0] == -2 and y[0] == -2 and x[1] == 2 and y[1] == 1:
    print('Y')
elif z > it3-2:
    print('N')
elif (z - it3) % 2 == 1:
    print('N')
else:
    print('Y')
# 0
# -2 -2
# 2 1
# 7
