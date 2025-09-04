for z in range(100):
    if (2 ** z - z) % 3 == 0 and (3 ** z - z) % 5 == 0 and (5 ** z - z) % 2 == 0:
        print(z)
        brea