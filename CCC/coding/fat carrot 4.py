n = 0
fat = 0
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                if a == d and b == c:
                    n += 1
                    if (a*1000+b*100+c*10+d) % 7 == 0:
                        fat += 1

print(n)
print(fat)
