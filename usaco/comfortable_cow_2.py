
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
lis = [[0]*1010]*1010
ans = 0


def check(x, y):
    if x<0 or y<0:
        return 0
    if x>=n or y>=n:
        return 0
    if lis[x][y] == 0:
        return 0
    cnt = 0
    for i in range(1, 5):
        xx = int(x + dx[i])
        yy = int(y + dy[i])
        if xx >= 0 and xx<n and yy>=0 and yy<n:
            # print("xx",xx,"yy",yy,lis[xx][yy])
            cnt += lis[xx][yy]
    # if cnt!=3:
    #     return 0
    # else:
    #     print("x,y",x,y)
    #     return 1
    return (cnt == 3)
def count(x, y):
    ans1 = 0
    ans2 = 0
    for i in range(5):
        ans1 += check(x+dx[i], y+dy[i])
    lis[x][y] = 1
    for i in range(5):
        ans2 += check(x+dx[i], y+dy[i])
    return ans2-ans1


n = int(input())
for a in range(n):
    s = list(map(int, input().split(" ")))
    x = s[0]
    y = s[1]
    ans += count(x, y)
    print(ans)