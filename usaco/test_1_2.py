n = int(input())
each_current_gift_lis = [-1]  # in 1-> 1, in 2->2,... in n -> n
each_cow_wishlist = [-1]  #[-1, [1,2,3,4], [], ... []]

# put everything in lis
for i in range(1, n+1):
    wishlist = list(map(int, input().split()))
    each_current_gift_lis.append(i)
    each_cow_wishlist.append(wishlist)
# check if anyone willing to trade
for i in range(1, n + 1):
    a_cow_num = i
    a_current_gift = each_current_gift_lis[i]
    a_cow_wishlist = each_cow_wishlist[i]
    a_current_gift_index = a_cow_wishlist.index(a_current_gift)
    for h in range(0, a_current_gift_index):
        wish_gift = a_cow_wishlist[h]
        for j in range(i+1, n+1):
            b_cow_num = j
            b_current_gift = each_current_gift_lis[j]
            if b_current_gift == wish_gift:
                b_cow_wishlist = each_cow_wishlist[j]
                b_current_gift_index = b_cow_wishlist.index(b_current_gift)
                if b_current_gift_index > b_cow_wishlist.index(a_current_gift):
                    temp = a_current_gift
                    each_current_gift_lis[i] = each_current_gift_lis[j]
                    each_current_gift_lis[j] = temp

for i in range(1,n+1):
    print(each_current_gift_lis[i])




