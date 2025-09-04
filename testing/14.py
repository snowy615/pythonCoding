for i in range(1, 1000):
    for j in range(1, 10000):
        if 1/i - 1/j == 1/2022 or 1/i - 1/j == -1/2022:
            print(i, j)