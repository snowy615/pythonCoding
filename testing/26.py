def is_prime(j):
    for i in range(2, int(j/2)):
        if j%i == 0:
            return False
    return True
n = int(input())
prime = []
for j in range(2, 100000):
    if is_prime(j) == True:
        prime.append(j)
for j in range(n):
    i = 0
    p = int(input())
    while prime[i] < 2*p:
        if 2*p-prime[i] in prime:
            print(prime[i], 2*p-prime[i])
            break
        i+=1
