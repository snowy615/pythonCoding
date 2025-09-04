lis = []
for i in range(400):
    lis.append(i)
x = 148
cnt = 0
while True:
    if cnt >= 100:
        print(x)
        break
    if x in lis:
        cnt += 1
        lis.remove(x)
        x -= 9
    if x <= 0:
        x += 400
