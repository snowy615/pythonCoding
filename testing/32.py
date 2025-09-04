import math
while True:
    r = int(input())
    if r == 0:
        break
    r2 = r*r
    count = r*4+1
    count2 = 0
    for i in range(1, r):
        count2 += int(math.sqrt(r2-i*i))
    print(count+count2*4)
