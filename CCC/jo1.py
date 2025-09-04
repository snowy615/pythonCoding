import time

def Josh(person, k, index):
    # Base case: when only one person is left
    if len(person) == 1:
        print(person[0])
        return

    # Find the index of the first person who will die
    index = (index + k) % len(person)

    # Remove the person who is going to be killed
    person.pop(index)

    # Recursive call for n-1 persons, with the new index
    Josh(person, k, index)


# Driver Program to test above function
n = 1000  # Number of people
k = 2   # Every k-th person is eliminated
k -= 1  # (k-1)th person will be killed because indexing starts from 0

index = 0

# Fill the person list
person = [i for i in range(1, n + 1)]

# Start timing
start_time = time.time()

# Call the Josephus function
Josh(person, k, index)

# Calculate runtime
end_time = time.time()
runtime = end_time - start_time

print(f"Runtime: {runtime:.6f} seconds")
