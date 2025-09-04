import time

# Measure start time
start_time = time.time()


def findTheWinner(n, k):
    # Base case
    if n == 1:
        return 0  # Return 0-based index

    # Recursive step
    return (findTheWinner(n - 1, k) + k) % n


# Wrapper to convert to 1-based indexing
def findTheWinner1Based(n, k):
    return findTheWinner(n, k) + 1


# Test the function
print(findTheWinner1Based(10, 2))

# Measure end time
end_time = time.time()
runtime = end_time - start_time

print(f"Runtime: {runtime:.6f} seconds")
