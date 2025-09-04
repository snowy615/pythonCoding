# 1 X n
# 2 X
# 3 X Y
# 4 X Y
# 5 X Y
# 6 X Y
# 7
A = 0
B = 0
z = input()
z = z.split()
l = []
while z[0] != '7':
    if z[0] == '1':
        if z[1] == 'A':
            A = int(z[2])
        if z[1] == 'B':
            B = int(z[2])
    if z[0] == '2':
        if z[1] == 'A':
            l.append(A)
        if z[1] == 'B':
            l.append(B)
    if z[0] == '3':
        if z[1] == 'A':
            A += B
        if z[1] == 'B':
            B += A
    if z[0] == '4':
        if z[1] == 'A':
            A *= B
        if z[1] == 'B':
            B *= A
    if z[0] == '5':
        if z[1] == 'A':
            if z[2] == 'A':
                A -= A
            if z[2] == 'B':
                A -= B
        if z[1] == 'B':
            if z[2] == 'A':
                B -= A
            if z[2] == 'B':
                B -= B
    if z[0] == '6':
        if z[1] == 'A':
            A = int(A/B)
        if z[1] == 'B':
            B = int(B/A)
    z = input()
    z = z.split()
for y in range(len(l)):
    print(l[y])