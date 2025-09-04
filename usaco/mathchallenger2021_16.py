for a in range(1, 7):
    for b in range(1, 163):
        for c in range(1, 163):
            if (a+1/(b+1/c)) == 2021/311:
                print(a, b, c, a+b+c)
