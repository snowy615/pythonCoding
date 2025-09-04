for i in range(1000):
    for j in range(10000):
        if i**2 == (671+j**2)/(3*(3+j**2)):
            print(i, j)