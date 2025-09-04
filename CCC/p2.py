t, n = map(int, input().split())
for i in range(t):
    hl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s=input()
    for j in range(n):
        if hl[ord(s[j])-97] < 2:
            hl[ord(s[j]) - 97] += 1
    for j in range(26):
        if hl[j] == 1:
            hl[j] = 0
        if hl[j] == 2:
            hl[j] = 1
    print(hl)
    first = hl[ord(s[0])-97]
    print(first)
    flag = True
    for j in range(1, n):
        first = (first+1) % 2
        print(f"checking criteria j {j} criteria {first} value {hl[ord(s[j])-97]}")
        if hl[ord(s[j])-97] != first:
            flag = False
            print("F")
            break
    if flag == True:
        print("T")

