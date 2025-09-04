import math
def polysum(n, s):
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    p = s * n
    return round(area + p**2, 4)