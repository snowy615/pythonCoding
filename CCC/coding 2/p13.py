def compareSfor2(pos_a, pos_b, pos_c):
    similarities_2 = []
    for i in pos_a:
        if (i in pos_b and i not in pos_c) or (i in pos_c and i not in pos_b):
            similarities_2.append(i)
    for i in pos_b:
        if (i in pos_a and i not in pos_c and i not in similarities_2) or (i in pos_c and i not in pos_a and i not in similarities_2):
            similarities_2.append(i)
    for i in pos_c:
        if (i in pos_a and i not in pos_b and i not in similarities_2) or (i in pos_b and i not in pos_a and i not in similarities_2):
            similarities_2.append(i)
    return similarities_2

def compareD3(pos_a, pos_b, pos_c):
    differences = []
    for i in pos_a:
        if i not in pos_b and i not in pos_c:
            differences.append(i)
    for i in pos_b:
        if i not in pos_a and i not in pos_c:
            differences.append(i)
    for i in pos_c:
        if i not in pos_b and i not in pos_a:
            differences.append(i)
    return differences

def compareD(pos_a, pos_b):
    differences = []
    for i in pos_a:
        if i not in pos_b:
            differences.append(i)
    for i in pos_b:
        if i not in pos_a:
            differences.append(i)
    return differences

def sumsNotCommon(intervals1, intervals2, intervals3):
    s = intervals1.split(" ")
    interval_1 = []
    pos_1 = []
    print(s)
    for i in range(0, len(s)):
        num = s[i].split(",")
        print(num)
        interval_1.append(int(num[0][1:]))
        interval_1.append(num[0][0])
        print(num[1][:-1])
        interval_1.append(int(num[1][:-1]))
        interval_1.append(num[1][-1])

        start = interval_1[i * 4]
        end = interval_1[i * 4 + 2]
        if interval_1[i * 4 + 1] == "(":
            start += 1
        if interval_1[i * 4 + 3] == "]":
            end += 1
        for i in range(start, end):
            if i not in pos_1:
                pos_1.append(i)
    print(interval_1)
    print(pos_1)

    s = intervals2.split(" ")
    interval_2 = []
    pos_2 = []
    print(s)
    for i in range(0, len(s)):
        num = s[i].split(",")
        print(num)
        interval_2.append(int(num[0][1:]))
        interval_2.append(num[0][0])
        print(num[1][:-1])
        interval_2.append(int(num[1][:-1]))
        interval_2.append(num[1][-1])

        start = interval_2[i * 4]
        end = interval_2[i * 4 + 2]
        if interval_2[i * 4 + 1] == "(":
            start += 1
        if interval_2[i * 4 + 3] == "]":
            end += 1
        for i in range(start, end):
            if i not in pos_2:
                pos_2.append(i)
    print(interval_2)
    print(pos_2)

    s = intervals3.split(" ")
    interval_3 = []
    pos_3 = []
    print(s)
    if s == ["null"]:
        differences = compareD(pos_1, pos_2)
        sum = 0
        for i in differences:
            sum += i
        return sum

    else:
        for i in range(0, len(s)):
            num = s[i].split(",")
            print(num)
            interval_3.append(int(num[0][1:]))
            interval_3.append(num[0][0])
            print(num[1][:-1])
            interval_3.append(int(num[1][:-1]))
            interval_3.append(num[1][-1])

            start = interval_3[i * 4]
            end = interval_3[i * 4 + 2]
            if interval_3[i * 4 + 1] == "(":
                start += 1
            if interval_3[i * 4 + 3] == "]":
                end += 1
            for j in range(start, end):
                if j not in pos_3:
                    pos_3.append(j)
        print(interval_3)
        print(pos_3)
        one = compareD3(pos_1, pos_2, pos_3)
        sum1 = 0
        for j in one:
            sum1 += j
        two = compareSfor2(pos_1, pos_2, pos_3)
        sum2 = 0
        for j in two:
            sum2 += j
        s = str(sum1) + " " + str(sum2)
        return s

