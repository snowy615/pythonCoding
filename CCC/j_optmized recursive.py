import time
start_time = time.time()

def findTheWinner(n, k):
    if n == 1:
        return 0
    if k == 1:
        return n - 1
    if k > n:
        return (findTheWinner(n - 1, k) + k) % n

    cnt = n // k
    res = findTheWinner(n - cnt, k)
    res -= n % k
    if res < 0:
        res += n
    else:
        res += res // (k - 1)
    return res

def findTheWinner1Based(n, k):
    return findTheWinner(n, k) + 1

print(findTheWinner1Based(200, 2))


end_time = time.time()
runtime = end_time - start_time
print("optimized recursive")
print(f"Runtime: {runtime:.6f} seconds")

