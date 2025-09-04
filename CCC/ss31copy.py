def find_optimal(color, pretty):
    max_values_c = []
    max_values_index = []
    for i in range(M+1):
        max_values_c.append(0)
        max_values_index.append(0)
    for x in range(1, N+1):
        if max_values_c[color[x]] < pretty[x]:
            max_values_c[color[x]] = pretty[x]
            max_values_index[color[x]] = x
        if pretty[x] > max_values_c[0] and x not in max_values_index:
            max_values_c[0] = pretty[x]
            max_values_index[0] = x
        print(f"---- x = {x}")
        print(max_values_c)
        print(max_values_index)

    max_sum = 0
    min_val = min(max_values_c)
    for i in range(1, M+1):
        max_sum += max_values_c[i]
    if min_val < max_values_c[0]:
        max_sum += max_values_c[0]-min_val
    return max_sum

N, M, Q = map(int, input().split())
color = [0]
pretty = [0]
for x in range(N):
    c, p = map(int, input().split())
    color.append(c)
    pretty.append(p)

print(color)
print(pretty)

print(find_optimal(color, pretty))

for x in range(Q):
    cp_change_type, i, cp = map(int, input().split())
    if cp_change_type == 1:
        color[i] = cp
        print(find_optimal(color, pretty))

    else:
        pretty[i] = cp
        print(find_optimal(color, pretty))




