n, k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_u = [0 for i in range(n)]
b_u = [0 for j in range(n)]
cnt = 0
for i in range(n):
    for j in range(i+k, n):
        print(cnt, i, j)
        print()
        print(a)
        print()
        print(a_u)
        print()
        print(b)
        print()
        print(b_u)
        print()
        print("------------------------------")
        if a_u[i] == 1:
            print("exit")
            break
        if a[i] + b[j] == m and b_u[i] == 0:
            print("in")
            a_u[i] = 1
            b_u[j] = 1
            cnt += 1
            break

for i in range(n):
    for j in range(i+k, n):
        print(cnt, i, j)
        print()
        print(a)
        print()
        print(a_u)
        print()
        print(b)
        print()
        print(b_u)
        print()
        print("------------------------------")
        if b_u[i] == 1:
            print("exit")
            break

        if a[j] + b[i] == m and a_u[j] == 0:
            print("in")
            a_u[j] = 1
            b_u[i] = 1
            cnt += 1
            break
print(cnt)