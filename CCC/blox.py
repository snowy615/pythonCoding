import itertools

def check(combo):
    for t in combo:
        if sum(list(t)) == height:
            return True
    return False
n = int(input())
for i in range(n):
    lis = list(map(int, input().split()))
    height = int(input())
    nums = len(lis)
    ts = 0
    for j in range(nums-1, -1, -1):
        if lis[j] > height:
            lis.pop(j)
        else:
            ts += lis[j]
    if ts < height:
        print("Not on my Blox")
    elif ts == height:
        print("Blox be crazy")
    else:
        r = 1
        while True:
            if r > nums:
                print("Not on my Blox")
                break
            combo = itertools.combinations(lis, r)
            if check(combo):
                print("Blox be crazy")
                break
            r += 1


