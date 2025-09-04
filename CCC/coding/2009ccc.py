fish1 = int(input())
fish2 = int(input())
fish3 = int(input())
num = int(input())
total = 0
for z in range(int(num/fish1)+1):
    for y in range(int(num/fish2)+1):
        for x in range(int(num/fish3)+1):
            if z==y==x==0:
                total+=0
            elif z*fish1 + y*fish2 + x*fish3 <= num:
                print('%s Brown Trout, %s Northern Pike, %s Yellow Pickerel' % (z, y, x))
                total += 1
print('Number of ways to catch fish: %s' % total)