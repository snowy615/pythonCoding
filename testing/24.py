from collections import defaultdict

x = int(input())
same = defaultdict(set)
different = defaultdict(set)
violations = 0

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
    group = [first, second, third]

    # check all of firsts needed are in group
    for member in group:
        for expected in same[member]:
            if expected not in group:
                violations += 1

        for notexpected in different[member]:
            if notexpected in group:
                violations += 1

print(violations // 2)


