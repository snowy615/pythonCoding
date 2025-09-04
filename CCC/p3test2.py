n = int(input())
alis = list(map(int, input().split()))
blis = list(map(int, input().split()))
ause = []
apt = 0
possible = True
for bpt in range(n):
    while True:
        if apt >= n:
            possible = False
            break
        if alis[apt] == blis[bpt]:
            if apt not in ause:
                ause.append(apt)
            break
        apt += 1
#finished setting up

if possible == False:
    print("NO")
else:
    print("YES")

    if alis == blis:
        print(0)
    x = 0
    while alis != blis and x < 20:
        if x > 12:
            break
        print(ause)
        for a in range(len(ause)):
            if alis == blis:
                break
            apt_c = ause[a]
            val = apt_c
            #index for useful numbers
            if a == 0:
                minNum = -1
            else:
                minNum = ause[a-1]
            print(f"useful index {apt_c} min {minNum}")
            for i in range(minNum+1, apt_c):
                alis[i] = alis[apt_c]
                if blis[i] == alis[apt_c]:
                    val = i
            if blis[apt_c] == alis[apt_c]:
                    val = apt_c
            ause.remove(apt_c)
            ause.append(val)
            ause.sort()
            print(f"val {val}")
            print(ause)
            print(alis)

            if minNum+1 != apt_c:
                print(f"L {minNum+1} {apt_c}")
        for a in range(len(ause)-1, -1, -1):
            if alis == blis:
                break
            apt_c = ause[a]
            val = apt_c
            if a == len(ause)-1:
                maxNum = n
            else:
                maxNum = ause[a+1]
            print(f"useful index {apt_c} min {minNum}")
            for i in range(maxNum-1, apt_c, -1):
                alis[i] = alis[apt_c]
                if blis[i] == alis[apt_c]:
                    val = i
            ause.remove(apt_c)
            ause.append(val)
            ause.sort()
            print(f"val {val}")
            print(ause)
            print(alis)
            if maxNum-1 != apt_c:
                print(f"R {apt_c} {maxNum -1}")

        x+=1