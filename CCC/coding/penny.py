# 3, 5, 6, 7, 9
count = 0
for a in range(1, 36):
    for b in range(1, 21):
        for c in range(1, 20):
            for d in range(1, 20):
                for e in range(1, 13):
                    if 3*a + 5*b + 6*c + 7*d + 9*e == 100:
                        print(a, b, c, d, e)
                        count += 1

print(count)