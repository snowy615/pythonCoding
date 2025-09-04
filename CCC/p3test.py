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
    print(ause)
    for a in range(len(ause)):
        apt_c = ause[a]
        if a == len(ause)-1:
            minNum = -1
        else:
            minNum = ause[a-1]
        pt = apt_c-1
        while True:
            if pt < minNum or blis[pt] != alis[apt_c]:
                break
            alis[pt] = alis[apt_c]
            pt -= 1
        if pt+1 != apt_c:
            print(f"L {pt+1} {apt_c}")
    for a in range(len(ause)-1, -1, -1):
        apt_c = ause[a]
        if a == len(ause)-1:
            maxNum = n
        else:
            maxNum = ause[a+1]
        pt = apt_c+1
        while True:
            if pt >= maxNum or blis[pt] != alis[apt_c]:
                break
            alis[pt] = alis[apt_c]
            pt += 1
        if pt -1 != apt_c:
            print(f"R {apt_c} {pt-1}")