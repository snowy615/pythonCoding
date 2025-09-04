a = int(input())
b = int(input())
c = int(input())
d = int(input())
price = 0
if a == 1:
    price += 461
elif a == 2:
    price += 431
elif a == 3:
    price += 420
else:
    price += 0
if b == 1:
    price += 100
elif b == 2:
    price += 57
elif b == 3:
    price += 70
else:
    price += 0
if c == 1:
    price += 130
elif c == 2:
    price += 160
elif c == 3:
    price += 118
else:
    price += 0
if d == 1:
    price += 167
elif d == 2:
    price += 266
elif d == 3:
    price += 75
else:
    price += 0
print('Your total Calorie count is %s.'%(price))