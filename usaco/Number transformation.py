for x in range(1,6):
    l = list(map(int, input().split()))
    p = l[1]
    num = list(map(int, list(str(l[0]))))
    n = len(num)
    p_num = num[n-p]
    for i in range(n-p):
        num[i] = (num[i]+p_num)%10
    for i in range(n-p+1, n):
        num[i] = abs(num[i]-p_num)
    print(f"{x}. ", end="")
    for i in range(n):
        print(num[i], end="")
    print("")
