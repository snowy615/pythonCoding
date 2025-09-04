from itertools import product

def generate_sequences():
    sequences = []
    for length in range(10):  # Including 0 to n digits
        for sequence in product('01', repeat=length):
            sequences.append(''.join(sequence))
    return sequences

def evaluate(sequence):
    # Convert the sequence string into a list of integers
    s = [int(char) for char in sequence]
    # Base case: if the sequence is reduced to one number, return it
    if len(s) <= 1:
        return s[0]
    new_s = []
    # Create a new sequence based on the evaluation rule
    for i in range(len(s)-1):
        new_s.append((s[i]+s[i+1]) % 2)
    # Recursively evaluate the new sequence
    return evaluate(new_s)

# Generating the sequences
sequences = generate_sequences()

# Optionally, you can print all the sequences to see them
for i in range(1, len(sequences)):
    print(sequences[i])
    ans = evaluate(sequences[i])
    print(ans)
    print("\n")
