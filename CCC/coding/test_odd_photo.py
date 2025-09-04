n = int(input())
l = list(map(int, input().split()))
lis = []
for i in l:
    if i % 2 == 0:
        lis.append(0)
    else:
        lis.append(1)
even = lis.count(0)
odd = lis.count(1)
if even > odd:
    print(odd*2)
if even < odd:
    while True:
        if even >= odd:
            break
        lis.remove(1)
        lis.remove(1)
        lis.append(0)
        even += 1
        odd -= 2
    print(lis)
    if even > odd:
        print(odd * 2)
    else:
        print(even+odd)
