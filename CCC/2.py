n, a, b = map(int, input().split())
ta = n
tb = n
for i in range(n):
    a1, b1 = map(int, input().split())
    if a1 >= a:
        ta += 1
    if b1 >= b:
        tb += 1
print(ta, tb)
if ta < tb:
    print("Andrew wins!")
elif tb < ta:
    print("Tommy wins!")
else:
    print("Tie!")