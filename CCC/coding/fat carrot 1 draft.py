numberoftimes = int(input())
b = 0
c = int(input())
for i in range(numberoftimes):
    for x in range(1,c):
        if c % x == 0:
            b += x
    if b == c:
        print("%s is a perfect number."%(c))
    elif b < c:
        print("%s is a deficient number."%(c))
    else:
        print("%s is a abundant number." %(c))