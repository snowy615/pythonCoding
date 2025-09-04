lis = []
for i in range(1, 2022):
    for j in range(1, 2022):
        if 4*i*j == (i+j)*(i+j-1) and i+j <= 2022:
            print(i, j)
            lis.append(i+j)
print(lis)
print(len(lis)/2)