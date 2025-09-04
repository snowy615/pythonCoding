import math
x = 1
for i in range(1, 51):
    x *= math.sqrt(math.sqrt(2^i))-i*math.sqrt(2*i)
print(x)