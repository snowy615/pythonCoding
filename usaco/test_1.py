n = int(input())
current_gift_lis = [-1]  # in 1-> 1, in 2->2,... in n -> n
each_cow_wishlist = [-1]  # 1st cow 1, 2... n        2nd cow n+1, n, ... 2n

# put everything in lis
for i in range(n):
    wishlist = list(map(int, input().split()))
    current_gift_lis.append(i + 1)
    for j in range(n):
        each_cow_wishlist.append(wishlist[j])
# check if anyone willing to trade
for i in range(1, n+1):
    a_cow_num = i
    a_current_gift = current_gift_lis[i]
    for j in range((i-1) * n, i * n):
        if each_cow_wishlist[j] == a_current_gift:
            a_current_gift_ranking = j-(i-1) * n
            break
    for j in range((i-1) * n, a_current_gift_ranking+(i-1) * n):
        


