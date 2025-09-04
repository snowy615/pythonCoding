def count(x, y, x_num, y_num):
    count_num = 0
    for i in range(len(x)):
        if x_num == x[i] and (y[i] == y_num-1 or y[i] == y_num+1):
            count_num += 1
        if y_num == y[i] and (x[i] == x_num-1 or x[i] == x_num+1):
            count_num += 1
    #print("count num{}".format(count_num))
    if count_num == 3:
        return True
    return False

n = int(input())
x = []
y = []
for a in range(n):
    s = list(map(int, input().split()))
    x.append(s[0])
    y.append(s[1])
    co = 0
    for b in range(len(x)):
        ha = count(x, y, x[b], y[b])
        if ha == True:
            co += 1
    print(co)