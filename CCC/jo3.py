#recursion
# Python code for Josephus Problem
import time
start_time = time.time()

def josephus(n, k):

    if (n == 1):
        return 1
    else:

        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        return (josephus(n - 1, k) + k-1) % n + 1

# Driver Program to test above function


n = 800
k = 2

print(josephus(n, k))
end_time = time.time()
runtime = end_time - start_time

print(f"Runtime: {runtime:.6f} seconds")
# This code is contributed by
# Sumit Sadhakar