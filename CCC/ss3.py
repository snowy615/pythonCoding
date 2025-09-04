def find_optimal(color, pretty):
    max_values_c = []
    max_values_index = []
    for i in range(M+1):
        max_values_c.append(0)
        max_values_index.append(0)
    for x in range(N):
        if max_values_c[color[x]] < pretty[x]:
            max_values_c[color[x]] = pretty[x]
            max_values_index[color[x]] = x+1
            # print(color[x])
            # print(max_values_c[color[x]])
            # print(pretty[x])
            # print(max_values_c)
            # print(max_values_index)
            # print("--")
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
color = []
pretty = []
for x in range(N):
    c, p = map(int, input().split())
    color.append(c)
    pretty.append(p)

print(color)
print(pretty)
print(find_optimal(color, pretty))

