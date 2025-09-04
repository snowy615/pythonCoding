h = int(input())
m = int(input())
a = 0
for t in range(1, m):
    if (-6)*t**4 + h*t**3 + 2*t**2 + t <= 0:
        print('The balloon first touches ground at hour:')
        print(t)
        a += 1
        break
    t += 1
if a == 0:
    print('The balloon does not touch ground in the given time.')
