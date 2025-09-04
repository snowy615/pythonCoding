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
    skip = 0
    group = list(input().split())
    a = group[0]
    b = group[1]
    c = group[2]
    for j in range(0, x*2, 2):
        if (together[j] == a or together[j] == b or together[j] == c):
            #print(together[j], together[j + 1])
            if (together[j+1] == a or together[j+1] == b or together[j+1] == c):
                pass
            else:
                skip = 1
        if (together[j+1] == a or together[j+1] == b or together[j+1] == c):
            #print(together[j + 1], together[j])
            if (together[j] == a or together[j] == b or together[j] == c):
                pass
            else:
                skip = 1
    for j in range(0, y*2, 2):
        if (not_together[j] == a or not_together[j] == b or not_together[j] == c) and (not_together[j+1] == a or not_together[j+1] == b or not_together[j+1] == c):
            skip = 1
    if skip == 1:
        vio_count += 1

print(vio_count)