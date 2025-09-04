a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 8 or a == 9:
    if d == 8 or d == 9:
        if b == c:
            print('ignore')
        else:
            print('answer')
    else:
        print('answer')
else:
    print('answer')
