import random
bag = ["r", "r", "r", "r", "r", "r", "r", "r", "b", "b","b", "b", "b", "b","b", "b", "g",  "g", "g", "g", "g",  "g", "g", "g"]
l_cnt = [0, 0, 0, 0,0, 0, 0, 0,0, 0, 0, 0,0]
for i in range(100000):
    random.shuffle(bag)
    cnt = []
    r=0
    b=0
    g=0
    for j in range(12):
        if bag[j] == "r":
            r+=1
        if bag[j] == "b":
            b+=1
        if bag[j] == "g":
            b+=1
    cnt.append(r)
    cnt.append(b)
    cnt.append(g)
    cnt.sort()
    if cnt == [0, 4, 8]:
        l_cnt[0] += 1
    if cnt == [1, 3, 8]:
        l_cnt[1] += 1
    if cnt == [2, 2, 8]:
        l_cnt[2] += 1
    if cnt == [0, 5, 7]:
        l_cnt[3] += 1
    if cnt == [1, 4, 7]:
        l_cnt[4] += 1
    if cnt == [2, 3, 7]:
        l_cnt[5] += 1
    if cnt == [0, 6, 6]:
        l_cnt[6] += 1
    if cnt == [1, 5, 6]:
        l_cnt[7] += 1
    if cnt == [2, 4, 6]:
        l_cnt[8] += 1
    if cnt == [3, 3, 6]:
        l_cnt[9] += 1
    if cnt == [2, 5, 5]:
        l_cnt[10] += 1
    if cnt == [3, 4, 5]:
        l_cnt[11] += 1
    if cnt == [4, 4, 4]:
        l_cnt[12] += 1
for i in range(13):
    print(i, l_cnt[i]/1000)
