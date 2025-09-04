n1 = int(input())
n2 = int(input())
l = []
l1 = []
for z in range(n1):
    word = input()
    l.append(word)
for y in range(n2):
    word = input()
    l1.append(word)
# print(l)
# print(l1)
for x in range(n1):
    for xx in range(n2):
        print(l[x] + ' as ' + l1[xx])
