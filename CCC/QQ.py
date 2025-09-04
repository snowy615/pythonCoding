def find_optimal(color, pretty):
    max_values_c = [] #1-indexed
    max_values_index = [] #1-indexed
    for i in range(M+1):
        max_values_c.append(0)
        max_values_index.append(0)
    for x in range(N):
        if max_values_c[color[x]] < pretty[x]:
            max_values_c[color[x]] = pretty[x]
            max_values_index[color[x]] = x+1
        if pretty[x] > max_values_c[0] and x+1 not in max_values_index:
            max_values_c[0] = pretty[x]
            max_values_index[0] = x+1
    max_sum = 0

    for i in range(1, M+1):
        max_sum += max_values_c[i]
    if min(max_values_c) < max_values_c[0]:
        max_sum += max_values_c[0]-min(max_values_c)
    return max_sum

N, M, Q = map(int, input().split())
color = [0]
pretty = [0]
for x in range(N):
    c, p = map(int, input().split())
    color.append(c)
    pretty.append(p)

print(find_optimal(color, pretty))




