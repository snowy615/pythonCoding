it = ''
l = []
num = 0
while True:
    it = input()
    num += 1
    if it == 'quit!':
        break
    elif len(it) <= 4:
        l.append(it)
    elif it[it.index('or')-1] == 'a' or it[it.index('or')-1] == 'e' or it[it.index('or')-1] == 'i' or it[it.index('or')-1] == 'o' or it[it.index('or')-1] == 'u' or it[it.index('or')-1] == 'y':
        l.append(it)
    elif it.index('or') + 2 != len(it):
        l.append(it)
    else:
        it = it[:len(it)-2] + 'our'
        l.append(it)

# print(l)
for z in range(num-1):
    print(l[z])