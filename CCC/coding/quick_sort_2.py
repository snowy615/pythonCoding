def quick_sort(lis, l, r):
    if l >= r:
        return
    i = l-1
    j = r+1
    x = lis[l+r >> 1]
    while i<j:
        while True:
            if lis[i] >= x:
                break
        while True:
            if lis[j] <= x:
                break
        if i < j:
            tmp = lis[i]
            lis[i] = lis[j]
            lis[j] = tmp
    quick_sort(lis, l, j)
    quick_sort(lis, j+1, r)
