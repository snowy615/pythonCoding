x = int(input())
friend = {}
enemy = {}
for i in range(x):
    temp_1 = input()
    temp_2 = input()
    if temp_1 in friend:
        friend.get(temp_1).append(temp_2)
    else:
        friend[temp_1] = [temp_2]

    if temp_2 in friend:
        friend.get(temp_2).append(temp_1)
    else:
        friend[temp_2] = [temp_1]
y = int(input())
for i in range(y):
    temp_1 = input()
    temp_2 = input()
    if temp_1 in enemy:
        enemy.get(temp_1).append(temp_2)
    else:
        enemy[temp_1] = [temp_2]

    if temp_2 in enemy:
        enemy.get(temp_2).append(temp_1)
    else:
        enemy[temp_2] = [temp_1]
