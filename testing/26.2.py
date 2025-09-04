from math import sqrt
def is_prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num %i == 0:
            return False
    return True
def solve(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(2*n-i):
            print(i, 2*n-i)
            return
x = int(input())
for i in range(x):
    n = int(input())
    solve(n)
