n = int(input())
current_gift_lis = [] #in 0-> 1, in 1->2,... in n-1 -> n
each_cow_wishlist = [] #1st cow 0, 1, 2... n-1        2nd cow n, n+1, ... 2n-1
#2*n-2, 3*n-1

#put everything in lis
for i in range(n):
    wishlist = list(map(int, input().split()))
    current_gift_lis.append(i+1)
    for j in range(n):
        each_cow_wishlist.append(wishlist[j])
#check if anyone willing to trade
for i in range(n):
    cow_num = i+1
    current_gift = current_gift_lis[i]
    for j in range(2*n-2, 3*n-1):


