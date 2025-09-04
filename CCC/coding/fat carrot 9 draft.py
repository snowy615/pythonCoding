a = []
for z in range(52):
    b = input()
    a.append(b)
for y in range(len(a)):
    c = y
    if a[y] == 'ace':
        while a[y+1] != 'ace' and a[y+1] != 'king' and a[y+1] != 'queen' and a[y+1] != 'jack':
            y += 1
            if y == c+4:
                print('Player X scores 4 point(s).')
    if a[y] == 'king':
        while a[y+1] != 'ace' and a[y+1] != 'king' and a[y+1] != 'queen' and a[y+1] != 'jack':
            y += 1
            if y == c+3:
                print('Player X scores 3 point(s).')
    if a[y] == 'queen':
        while a[y+1] != 'ace' and a[y+1] != 'king' and a[y + 1] != 'queen' and a[y + 1] != 'jack':
            y += 1
            if y == c+2:
                print('Player X scores 2 point(s).')
    if a[y] == 'jack':
        while a[y+1] != 'ace' and a[y+1] != 'king' and a[y + 1] != 'queen' and a[y + 1] != 'jack':
            y += 1
            if y == c+1:
                print('Player X scores 1 point(s).')