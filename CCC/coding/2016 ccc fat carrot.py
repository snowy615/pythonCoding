score = 0
for i in range(6):
    a = input()
    if a == 'W':
        score += 1
if score == 0:
    print(-1)
elif score == 1 or score == 2:
    print(3)
elif score == 3 or score == 4:
    print(2)
else:
    print(1)