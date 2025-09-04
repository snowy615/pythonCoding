def merge_sort(lis):
    if len(lis) <= 1:
        return
    mid = len(lis)//2
    l = lis[:mid]
    r = lis[mid:]
    merge_sort(l)
    merge_sort(r)
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            lis[k] = l[i]
            i += 1
        else:
            lis[k] = r[j]
            j += 1
        k+=1
    while i < len(l):
        lis[k] = l[i]
        i += 1
        k += 1
    while j < len(l):
        lis[k] = r[j]
        j+=1
        k+=1
n = int(input())
lis = list(map(int, input().split()))
merge_sort(lis)
for i in lis:
    print(i, end=" ")