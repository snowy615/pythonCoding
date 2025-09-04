def add(l, x):
    t = [1, 1, 2, 3, 5]
    global hour, min
    if l == "R":
        hour += t[x]
    elif l == "B":
        hour += t[x]
        min += t[x]
    elif l == "G":
        min += t[x]

for j in range(5):
    l = input().split()
    hour = 0
    min = 0
    for x in range(5):
        add(l[x], x)
    min *= 5
    if min == 60:
        hour += 1
        min = 0
    if hour >= 12:
        hour -= 12

    if hour < 10:
        print(f"0{hour}", end=":")
    else:
        print(hour, end=":")

    if min < 10:
        print(f"0{min}")
    else:
        print(min)
