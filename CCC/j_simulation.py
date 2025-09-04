import time
start_time = time.time()

def findTheWinner(n, k):
    circle = list(range(1, n + 1))
    start_index = 0
    while len(circle) > 1:
        removal_index = (start_index + k - 1) % len(circle)
        circle.pop(removal_index)
        start_index = removal_index
    return circle[0]

print(findTheWinner(1000, 2))
end_time = time.time()
runtime = end_time - start_time
print("Simulation")
print(f"Runtime: {runtime:.6f} seconds")
