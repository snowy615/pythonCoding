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

direction=["N","E","S","W"]
nowd=""
x=0
y=0
res=[]
def pengqiang(x,y):
    return floor[x][y]=="X"
def turnright(nowd):
    return direction[(direction.index(nowd)+1)%4]

def turnleft(nowd):
    return direction[(direction.index(nowd)+3)%4]





for i in range(r):
    for j in range(c):
        x=i
        y=j
        if floor[x][y]!="X":
            for nowd in direction:
                 count=0
                 x = i
                 y = j
                 # print("开始点", x, y)
                 # print("开始方向", nowd)
                 for k in frl:


                    if k=="F":
                        count+=1
                        if nowd == "N":
                            x -= 1
                            # print(x,y)

                        if nowd == "S":
                            x += 1
                            # print(x,y)


                        if nowd == "W":
                            y -= 1
                            # print(x,y)

                        if nowd == "E":
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
                        # print("右转")
                        nowd=turnright(nowd)

                    if k=="L":
                        count+=1
                        nowd=turnleft(nowd)
        else:
            continue
for i in range(r):
    for j in range(c):
        print(floor[i][j],end = '')
    print('')