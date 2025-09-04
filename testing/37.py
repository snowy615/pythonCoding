import math
for i in range(1, 100000):
    if (math.sqrt((i * (i+32)))+0.5) ** 2 == i * (i+32):
        print(i)