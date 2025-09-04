def f(n, c):
    if c == 5:
        return True
    n -= 1
    if n%5==0: return f(int(4*n/5), c+1)
    else: return False
for i in range(10000):
    if f(i*5+1, 0) == True: print(i*5+1)