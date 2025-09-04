vio_count = 0
x = int(input())
together = []
for i in range(x):
    names = list(input().split())
    together.append(names[0])
    together.append(names[1])
y = int(input())
not_together = []
for i in range(y):
    names = list(input().split())
    not_together.append(names[0])
    not_together.append(names[1])
z = int(input())
for i in range(z):
    group = list(input().split())
    a = group[0]
    b = group[1]
    c = group[2]
    if a in together:
        index = together.index(a)
        if index % 2==0 and (together[index+1] != b and together[index+1] != c):
            vio_count += 1
            print("a", i)
            continue
        if index % 2 == 1 and (together[index - 1] != b and together[index - 1] != c):
            vio_count += 1
            print("b", i)
            continue
    if b in together:
        index = together.index(b)
        if index % 2==0 and (together[index+1] != a and together[index+1] != c):
            vio_count += 1
            print('c')
            continue
        if index % 2 == 1 and (together[index - 1] != a and together[index - 1] != c):
            vio_count += 1
            print('d')
            continue
    if c in together:
        index = together.index(c)
        if index % 2==0 and (together[index+1] != b and together[index+1] != a):
            vio_count += 1
            #print('e')
            continue
        if index % 2 == 1 and (together[index - 1] != b and together[index - 1] != a):
            vio_count += 1
            #print('f', i)
            continue
    if a in not_together:
        index = not_together.index(a)
        if index % 2 == 0 and (not_together[index + 1] == b or not_together[index + 1] == c):
            vio_count += 1
            #print('g')
            continue
        if index % 2 == 1 and (not_together[index - 1] == b or not_together[index - 1] == c):
            vio_count += 1
            #print('h')
            continue
    if b in not_together:
        index = not_together.index(b)
        if index % 2 == 0 and (not_together[index + 1] == a or not_together[index + 1] == c):
            vio_count += 1
            #print('i')
            continue
        if index % 2 == 1 and (not_together[index - 1] == a or not_together[index - 1] == c):
            vio_count += 1
            #print('j')
            continue
    if c in not_together:
        index = not_together.index(c)
        if index % 2 == 0 and (not_together[index + 1] == b or not_together[index + 1] == a):
            vio_count += 1
            #print('k')
            continue
        if index % 2 == 1 and (not_together[index - 1] == b or not_together[index - 1] == a):
            vio_count += 1
            #print('l')
            continue
print(vio_count)