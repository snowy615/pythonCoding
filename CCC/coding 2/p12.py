s = input().split(" ")
interval_1 = []
pos_1 = []
print(s)
for i in range(0, len(s), 2):
    num = s[i].split(",")
    interval_1.append(int(s[i][1:]))
    interval_1.append(s[i][0])
    print(s[i+1][:-1])
    interval_1.append(int(s[i+1][:-1]))
    interval_1.append(s[i+1][-1])

    start = interval_1[i*4]
    end = interval_1[i*4+2]
    if interval_1[i*4+1] == "(":
        start += 1
    if interval_1[i*4+3] == ")":
        end -= 1
    for i in range(start, end):
        if i not in pos_1:
            pos_1.append(i)
print(interval_1)
print(pos_1)

