import time
start_time = time.time()

def findTheWinner(n, k):
    ans = 0
    for i in range(2, n + 1):
        ans = (ans + k) % i
    return ans + 1

print(findTheWinner(200, 2))

end_time = time.time()
runtime = end_time - start_time
print("iteration")
print(f"Runtime: {runtime:.6f} seconds")


