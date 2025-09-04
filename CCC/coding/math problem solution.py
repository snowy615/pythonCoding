total = 0
for a in range(5):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if a+b+c+d == 13 and (1000*a+100*b+10*c+d) % 11 == 0:
                    print(1000*a+100*b+10*c+d)
                    total += 1
print(total)