def quickSort(lis, l, r):
    if l >= r:
        return
    x = lis[l + r >> 1]
    i = l - 1
    j = r + 1
    while i < j:
        while True:
            i += 1
            if lis[i] >= x:
                break
        while True:
            j -= 1
            if lis[j] <= x:
                break
        if i < j:
            tmp = lis[i]
            lis[i] = lis[j]
            lis[j] = tmp

    quickSort(lis, l, j)
    quickSort(lis, j + 1, r)

def main():
    n = int(input())
    q = list(map(int, input().split()))
    quickSort(q, 0, n - 1)

    for i in range(n):
        print(q[i], end=' ')

main()






