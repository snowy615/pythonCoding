word = input()
letter = list(map(str, word))
a = 0
for i in range(len(letter)):
    if letter[i] not in ('I', 'O', 'S', 'H', 'Z', 'X', 'N'):
        print('NO')
        a += 1
        break
if a == 0:
    print('YES')