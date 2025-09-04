def d_winner(lis_one, lis_two):
    count_a = 0
    count_b = 0
    for i in range(4):
        for j in range(4):
            if lis_one[i] > lis_two[j]:
                count_a += 1
            if lis_two[j] > lis_one[i]:
                count_b += 1
    if count_a > count_b:
        return 1
    elif count_a < count_b:
        return 2
    else:
        return 0
def try_testcase():
    for i in range(10000):
        check = pos_val[i]
        if d_winner(A, check) == 2:
            if d_winner(B, check) == 1:
                print("yes")
                return

    print("no")
    return
pos_val = []
for w in range(1, 11):
    for x in range(1, 11):
        for y in range(1, 11):
            for z in range(1, 11):
                pos_val.append([w, x, y, z])
num = int(input())
for x in range(num):
    A_B = list(map(int, input().split()))
    A = A_B[:4]
    B = A_B[4:]
    winner_a_b = d_winner(A, B)
    if winner_a_b == 2:
        c = A
        A = B
        B = c
    try_testcase()