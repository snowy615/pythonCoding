def equalCount(clock, h, m, s):
    h_cnt = 0
    m_cnt = 0
    s_cnt = 0
    value = [1, 1, 2, 3, 5]
    for i in range(5):
        if clock[i] == 'y' or clock[i] == 'r' or clock[i] == 'w' or clock[i] == 'm':
            h_cnt += value[i]
        if clock[i] == 'y' or clock[i] == 'g' or clock[i] == 'w' or clock[i] == 'c':
            m_cnt += value[i]*5
        if clock[i] == 'm' or clock[i] == 'c' or clock[i] == 'w' or clock[i] == 'b':
            s_cnt += value[i]*5
        if h_cnt > h or m_cnt > m or s_cnt > s:
            return 2
    if h_cnt == h and m_cnt == m and s_cnt == s:
        return 1
    else:
        return 0

h, m, s = map(int, input().split(":"))
lis = []
cr = ['w', 'y', 'c', 'm', 'r', 'g', 'b', 'k']
for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    clock = [cr[a], cr[b], cr[c], cr[d], cr[e]]
                    cnt = equalCount(clock, h, m, s)
                    if cnt == 1:
                        lis.append(cr[a]+cr[b]+cr[c]+cr[d]+cr[e])
lis.sort()
print(lis)