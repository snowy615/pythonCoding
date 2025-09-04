num = int(input())
count = 0
for z in range(num):
    goal = int(input())
    foul = int(input())
    score = goal*5-foul*3
    if score > 40:
        count += 1
if count == num:
    print(f"{count}+")
else:
    print(count)