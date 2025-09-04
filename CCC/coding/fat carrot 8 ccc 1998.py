z = int(input())
for y in range(z):
    a = input()
    b = []
    c = ""
    b = a.split()
    for i in range(len(b)):
        if len(b[i]) == 4:
            b[i] = '****'
    for x in range(len(b)-1):
        c += b[x] + " "
    print(c + b[-1])
#I love to bite the fat little carrot nose