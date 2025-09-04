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
        print(name, V)
        if V > v_1:
            v_2 = v_1
            n_2 = n_1
            n_1 = name
            v_1 = V
        elif V > v_1:
            v_2 = v_1
            n_2 = n_1
            n_1 = name
            v_1 = V
        elif V > v_2:
            v_2 = V
            n_2 = name
        print(n_1, v_1, n_2, v_2)
    if v_1 == v_2:
        temp = [n_1, n_2]
        temp.sort()
        print(temp)
        print(temp[0])
        print(temp[1])
    else:
        print(n_1)
        print(n_2)