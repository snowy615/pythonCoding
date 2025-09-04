# import math
# import time
# start = time.time()
# total = 0
# for z in range(1, 2009):
#     a = math.sqrt(z * 72)
#     if a == round(a, 0):
#         print(z)
#         total += 1
# print(total)
# end = time.time()
# print(end-start)


l = []
for z in range(2008):
    l.append(1)
for y in range(1, 2009):
    num = int(2008 / y)
    for x in range(num):
        print(num * x)
l.count(1)