n = int(input())
if n == 1:
    str = input().split()
    print(str[0])
if n >= 2:
    n_1 = []
    n_2 = []
    v_1 = []
    v_2 = []
    for i in range(n):
        str = input().split()
        name = str[0]
        R = int(str[1])
        C = int(str[2])
        S = int(str[3])
        V = R*2+C*3+S
        n_1.append(name)
        v_1.append(V)
        v_2.append(V)
    v_2.sort()
    max = v_2[-1] #max value
    i = v_2.index(max) #last value index
    cnt = n-i
    for x in range(n):
        if v_1[x] == max:
            n_2.append(n_1[x])
    n_2.sort()
    print(n_2[0])
    if cnt>=2:
        print(n_2[1])
    else:
        n_2 = []
        max = v_2[i-1]
        for x in range(n):
            if v_1[x] == max:
                n_2.append(n_1[x])
        n_2.sort()
        print(n_2[0])