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
    if bool[order[i+1]] == 0:
        count += moo[order[i+1]]
        bool[cow_num] = 1
# print("break")
# print(count)
count_2 = 0
order.reverse()
bool = [0 for i in range(n+1)]
for i in range(1, n):
    cow_num = order[i]
    if bool[order[i + 1]] == 0:
        count_2 += moo[order[i + 1]]
        bool[cow_num] = 1
print(max(count, count_2))