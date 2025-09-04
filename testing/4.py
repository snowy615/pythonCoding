def prime(i):
    for j in range(2, i):
        if i%j==0:
            return False
    return True
for i in range(10000000, 100000000):
    if prime(i) == True:
        print(i)
#100000007