import time
start_time = time.time()

def findTheWinner(n, k):
    return winnerHelper(n, k) + 1

def winnerHelper(n, k):
    if n == 1:
        return 0
    return (winnerHelper(n - 1, k) + k) % n

print(findTheWinner(200, 2))
end_time = time.time()
runtime = end_time - start_time
print("recursion")
print(f"Runtime: {runtime:.6f} seconds")


