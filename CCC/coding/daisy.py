def find_average(lis, i, step):
    j = i + step
    total = 0
    for x in range(i, j+1):
        total += lis[x]
    average = total / (j-i+1)
    if average.is_integer() == False:
        return False
    #print(f"i{i} step{step} j{j} total{total} average{average}")
    while True:
        if average not in lis:
            return False
        for z in range(i, j+1):
            if lis[z] == average:
                return True
        return False

n = int(input())
lis = list(map(int, input().split()))
count = n
for step in range(1, n):
    for b in range(0, n-step):
        TF = find_average(lis, b, step)
        # print(TF)
        if TF == True:
            count += 1
print(count)
