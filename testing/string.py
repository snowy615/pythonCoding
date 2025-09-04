for x in range(5):
    s1, s2 = input().split()
    j = len(s2)-1
    l1= len(s1)
    l2 = len(s2)
    for i in range(l1):
        for y in range(j, 0, -1):
            print(f"i = {i} j = {j} y = {y} s2[y] = {s2[y]} s1[i] = {s1[i]}")
            if s2[y] == s1[i]:
                print(s1[i], end="")
                j = y
                break
    print()
    print("--------------------------")