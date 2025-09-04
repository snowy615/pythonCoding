n = int(input())
lis = list(map(int, input().split()))

def merge_sort(lis):
    if len(lis) <= 1:
        return
    mid = len(lis) // 2
    L = lis[:mid]
    R = lis[mid:]
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            lis[k] = L[i]
            i += 1
        else:
            lis[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        lis[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        lis[k] = R[j]
        k += 1
        j += 1

merge_sort(lis)
for i in lis:
    print(i, end=" ")
