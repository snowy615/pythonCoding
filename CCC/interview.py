n, k = map(int, input().split())
f = [0]*k
totalTime = 0
t = list(map(int, input().split()))
if k >= n:
    print(t[n])
    f[n] = 1
    s = ''.join([str(item) for item in f])
    print(f)
else:
    countdown = [] #keeping track of current cows being interviewed, [time left over, farmer]
    cf = [] #keeping track of the finished farmer at each state
    for i in range(n):
        countdown.append([t[i],i])
    #set up
    for x in range(n-k):
        countdown.sort()
        m = countdown[0][0]
        totalTime += m
        lis = []
        for i in range(n):
            countdown[i][0] -= m
            if countdown[i][0] == 0:
                lis.append(countdown[i][1])
                if x>1 and countdown[i][1] in cf[x-1]:
                    for j in cf:
                        if j not in lis:
                            lis.append(j)

        cf.append(lis)
        openFarmer = countdown[0][1]
        countdown.remove(countdown[0])
        countdown.append([t[x+k], openFarmer])

    for a in cf[-1]:
        f[a] = 1
    print(totalTime + t[-1])
    print(f)
