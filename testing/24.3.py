from collections import defaultdict
same = defaultdict(set)
different = defaultdict(set)
violation = 0

x = int(input())
for i in range(x):
    first, second = input().split()
    same[first].add(second)
    same[second].add(first)
y = int(input())
for i in range(y):
    first, second = input().split()
    different[first].add(second)
    different[second].add(first)

g = int(input())
for i in range(g):
    first, second, third = input().split()
    group = [first,second,third]
    for member in group:
        for expected in same[member]:
            if expected not in group:
                violation += 1
        for not_expected in different[member]:
            if not_expected in group:
                violation += 1
print(violation//2)
