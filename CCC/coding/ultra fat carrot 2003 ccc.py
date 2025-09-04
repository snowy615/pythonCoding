b = int(input())
c = int(input())
d = int(input())
for i in range(b):
    print('*'+' '*c+'*'+' '*c+'*')
print('***'+'*'*c*2)
for h in range(d):
    print(' '*(1+c)+'*')