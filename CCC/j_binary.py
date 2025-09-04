import time
start_time = time.time()

def findTheWinner(n):
    n_binary = bin(n)[2:]
    if len(n_binary) == 1:
        return n
    shifted = n_binary[1:] + n_binary[0]
    return int(shifted, 2)

print(findTheWinner(1000))


end_time = time.time()
runtime = end_time - start_time
print("binary")
print(f"Runtime: {runtime:.6f} seconds")

