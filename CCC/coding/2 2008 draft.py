song = ['A', 'B', 'C', 'D', 'E']
button1 = [1, 2, 3, 4, 0]
button2 = [4, 0, 1, 2, 3]
button3 = [1, 0, 2, 3, 4]
endd = 0
b1 = int(input())
num1 = int(input())
if b1 == 1:
    for z in range(num1):
       song = [song[y] for y in button1]
elif b1 == 2:
    for z in range(num1):
       song = [song[y] for y in button2]
elif b1 == 3:
    for z in range(num1):
       song = [song[y] for y in button3]
elif b1 == 4:
    for z in range(num1):
        for out in range(4):
           print(song[out], end = ' ')
        print(song[4])
        endd += 1
if endd == 0:
    b2 = int(input())
    num2 = int(input())
    z = 0
    y = 0
    if b2 == 1:
        for z in range(num2):
            song = [song[y] for y in button1]
    elif b2 == 2:
        for z in range(num2):
            song = [song[y] for y in button2]
    elif b2 == 3:
        for z in range(num2):
            song = [song[y] for y in button3]
    elif b2 == 4:
        for z in range(num2):
            for out in range(4):
                print(song[out], end = ' ')
            print(song[4])
            endd += 1
else:
    endd += 0
if endd == 0:
    b3 = int(input())
    num3 = int(input())
    z = 0
    y = 0
    if b3 == 1:
        for z in range(num3):
            song = [song[y] for y in button1]
    elif b3 == 2:
        for z in range(num3):
            song = [song[y] for y in button2]
    elif b3 == 3:
        for z in range(num3):
            song = [song[y] for y in button3]
    elif b3 == 4:
        for z in range(num3):
            for out in range(4):
                print(song[out], end = ' ')
            print(song[4])
            break
else:
    endd += 0
if endd == 0:
    b4 = int(input())
    num4 = int(input())
    z = 0
    y = 0
    if b4 == 1:
        for z in range(num4):
            song = [song[y] for y in button1]
    elif b4 == 2:
        for z in range(num4):
            song = [song[y] for y in button2]
    elif b4 == 3:
        for z in range(num4):
            song = [song[y] for y in button3]
    elif b4 == 4:
        for z in range(num4):
            for out in range(4):
                print(song[out], end = ' ')
            print(song[4])