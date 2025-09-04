for i in range(5):
    lis = input().split()
    s_num = list(lis[0])
    s_num.reverse()
    p_index = int(lis[1])
    p = int(s_num[p_index-1])
    for j in range(len(s_num)):
        if j > p_index-1:
            s_num[j] = str((p+int(s_num[j]))%10)
        if j < p_index-1:
            s_num[j] = str(abs(p-int(s_num[j])%10))
    s_num.reverse()
    for k in s_num:
        print(k, end="")
    print("")
