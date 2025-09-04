for x in range(1, 500):
    for y in range(x, 500):
        for z in range(y, 500):
            if x*y*z == 2*(x+y+z):
                print(x, y, z)