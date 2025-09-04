def countLargestDigit(num, base, start):
    s_num = list(map(int, str(start)))
    count = 0
    s_num.reverse()
    for j in range(num):
        print(f"n{j}")
        i = 0
        n = len(s_num)
        while True:
            if i >= n-1 and s_num[i] >= base:
                s_num[i] %= base
                s_num.append(1)
                break
            elif s_num[i] >= base:
                s_num[i] %= base
                i += 1
                s_num[i] += 1
            else:
                break
        count += s_num.count(base - 1)
        print(count)
        print(s_num)
        s_num[0] += 1
    return count
print(countLargestDigit(10, 5, 32))