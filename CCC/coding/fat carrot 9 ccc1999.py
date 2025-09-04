a = []
scoreA = 0
scoreB = 0
for z in range(52):
    b = input()
    a.append(b)
for y in range(len(a)-1):
    c = y
    if a[y] == 'ace':
        if y < 48:
            while a[y+1] != 'ace' and a[y+1] != 'king' and a[y+1] != 'queen' and a[y+1] != 'jack':
                y += 1
                if y == c+4:
                    if c % 2 == 0:
                        print('Player A scores 4 point(s).')
                        scoreA += 4
                        break
                    else:
                        print('Player B scores 4 point(s).')
                        scoreB += 4
                        break

    if a[y] == 'king':
        if y < 49:
            while a[y+1] != 'ace' and a[y+1] != 'king' and a[y+1] != 'queen' and a[y+1] != 'jack':
                y += 1
                if y == c+3:
                    if c % 2 == 0:
                        print('Player A scores 3 point(s).')
                        scoreA += 3
                        break
                    else:
                        print('Player B scores 3 point(s).')
                        scoreB += 3
                        break
    if a[y] == 'queen':
        if y < 50:
            while a[y+1] != 'ace' and a[y+1] != 'king' and a[y + 1] != 'queen' and a[y + 1] != 'jack':
                y += 1
                if y == c+2:
                    if c % 2 == 0:
                        print('Player A scores 2 point(s).')
                        scoreA += 2
                        break
                    else:
                        print('Player B scores 2 point(s).')
                        scoreB += 2
                        break
    if a[y] == 'jack':
        if y < 51:
            while a[y+1] != 'ace' and a[y+1] != 'king' and a[y + 1] != 'queen' and a[y + 1] != 'jack':
                y += 1
                if y == c+1:
                    if c % 2 == 0:
                        print('Player A scores 1 point(s).')
                        scoreA += 1
                        break
                    else:
                        print('Player B scores 1 point(s).')
                        scoreB += 1
                        break
        else:
            break
print('Player A: %s point(s).'%(scoreA))
print('Player B: %s point(s).'%(scoreB))