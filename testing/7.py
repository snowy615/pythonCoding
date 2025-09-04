def addFive(x):
    return x+5
def minFive(x):
    return x-5
x = 6
y = 10
z = 13

x = addFive(y)
print(x, y, z)
z = minFive(z)
print(x, y, z)
x += 10
print(x, y, z)
z = z+x
print(x, y, z)