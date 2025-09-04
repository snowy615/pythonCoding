lis = list(map(int, input().split()))
lis.sort()
max_num = lis[-1]
A = lis[0]
B_C = max_num-A
B = lis[1]
C = B_C - B
print(f"{A} {B} {C}")
