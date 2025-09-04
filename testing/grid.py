import math
lis_cnt = []
for i in range(100):
    lis_cnt.append(0)
for i in range(2, 500):
    for j in range(i+1, 500):
        cnt_i = 0
        cnt_j = 0
        for x in range(2, i+1):
            if math.gcd(i, x) > 1:
                cnt_i += 1
        for y in range(2, j+1):
            if math.gcd(j, y) > 1:
                cnt_j += 1
        final_cnt = i*j-cnt_i*j-cnt_j*i+cnt_j*cnt_i
        if final_cnt < 100:
            lis_cnt[final_cnt] += 1

        print(f"i {i}    j {j}    final_cnt {final_cnt}")
print(lis_cnt)