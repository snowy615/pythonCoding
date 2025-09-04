# N^2??? or N
import time
start_time = time.time()


def Josephus(n, k):
    k -= 1
    arr = [0] * n
    for i in range(n):
        arr[i] = 1  # Makes all the 'n' people alive by
        # assigning them value = 1
    cnt = 0
    cut = 0
    num = 1  # Cut = 0 gives the sword to 1st person.
    while (cnt < (n - 1)):

        # Loop continues till n-1 person dies.
        while (num <= k):

            # Checks next (kth) alive persons.
            cut += 1
            cut = cut % n  # Checks and resolves overflow
            # of Index.
            if (arr[cut] == 1):
                num += 1  # Updates the number of persons
                # alive.

        num = 1  # refreshes value to 1 for next use.
        arr[cut] = 0  # Kills the person at position of 'cut'
        cnt += 1  # Updates the no. of killed persons.
        cut += 1
        cut = cut % n  # Checks and resolves overflow of Index.
        while (arr[cut] == 0):
            # Checks the next alive person the
            # sword is to be given.
            cut += 1
            cut = cut % n  # Checks and resolves overflow
            # of Index.

    return cut + 1  # Output is the position of the last
    # man alive(Index + 1)


# Driver Code
n, k = 800000, 2  # map (int, input().splut())
print(Josephus(n, k))

# This code is contributed by ShubhamSingh
end_time = time.time()
runtime = end_time - start_time

print(f"Runtime: {runtime:.6f} seconds")

# This code is contributed by
# Gaurav Kandel