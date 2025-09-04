import sys
from collections import defaultdict
R = int(input())
C = int(input())
start = 0
D = defaultdict(set)
for x in range(1,R+1):
    line = input().split()
    for y in range(1, C+1):
        num = int(line[y-1])
        if (x, y) == (1, 1):
            start = num
        D[x*y].add(num)
if (R, C) == (1, 1):
    print("yes")
    sys.exit()

found = set()
Current = [start]
finish = R*C
while len(Current) > 0:
    current = Current.pop()
    if current == finish:
        print("yes")
        sys.exit()
    if current in found:
        continue
    found.add(current)
    Current.extend(D[current])
print("no")