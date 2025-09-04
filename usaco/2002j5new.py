floor=[]
r=int(input())
c=int(input())
for i in range(r):
    a=list(map(str,input()))
    floor.append(a)
n=int(input())
frl=[]
for i in range(n):
    frl.append(input())

if n>1000:
    print(n)
nowd=""
x=0
y=0
res=[]
def pengqiang(x,y):
    return floor[x][y]=="X"





for i in range(r):
    for j in range(c):
        x=i
        y=j
        if floor[x][y]=="X":
            break
        else:
            for nowd in range(4):
                 count=0
                 x = i
                 y = j
                 # print("开始点", x, y)
                 # print("开始方向", nowd)
                 for k in frl:


                    if k=="F":
                        count+=1
                        if nowd == 0:
                            x -= 1
                            # print(x,y)

                        if nowd == 2:
                            x += 1
                            # print(x,y)


                        if nowd == 3:
                            y -= 1
                            # print(x,y)

                        if nowd == 1:
                            y += 1
                            # print(x,y)
                        if x<0 or x>=r or y<0 or y>=c:
                            # print("出界")
                            break
                        if pengqiang(x, y):
                            # print("碰墙")
                            break
                        if count==n:
                            floor[x][y] = "*"
                            # print("标记")


                    if k=="R":
                        count+=1
                        nowd =(nowd+1)%4

                    if k=="L":
                        count+=1
                        nowd=(nowd+3)%4

for i in range(r):
    for j in range(c):
        print(floor[i][j],end = '')
    print('')