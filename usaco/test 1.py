n = int(input())
count = 0
moo = [0 for i in range(n+1)]
order = [0]
for i in range(n):
    s = list(map(int, input().split()))
    moo[s[0]] = s[1]
    order.append(s[0])
bool = [0 for i in range(n+1)]
for i in range(1, n):
    cow_num = order[i]
    if cow_num == n:
        if bool[order[1]] == 0:
            print(cow_num, moo[1])
            count += moo[order[1]]
            bool[cow_num] = 1
    else:
        if bool[order[cow_num]+1] == 0:
            print(cow_num, moo[cow_num+1])
            count += moo[cow_num+1]
            bool[cow_num] = 1
# print("break")
# print(count)
count_2 = 0
bool = [0 for i in range(n+1)]
for i in range(n, 0, -1):
    cow_num = order[i]
    if cow_num == n:
        if bool[1] == 0:
            #print(cow_num, moo[1])
            count_2 += moo[1]
            bool[cow_num] = 1
    else:
        if bool[cow_num + 1] == 0:
            #print(cow_num, moo[cow_num + 1])
            count_2 += moo[cow_num + 1]
            bool[cow_num] = 1
print(max(count, count_2))