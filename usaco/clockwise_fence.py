n = int(input())
for i in range(n):
    s = input()
    degree = 0
    for j in range(len(s)):
        J = (j+1)%len(s)
        if s[j] == s[J]:
            continue
        if (s[j] == "N" and s[J] == "E") or (s[j] == "E" and s[J] == "S") or (s[j] == "S" and s[J] == "W") or (s[j] == "W" and s[J] == "N"):
            degree += 90
            continue
        if (s[j] == "N" and s[J] == "W") or (s[j] == "E" and s[J] == "N") or (s[j] == "S" and s[J] == "E") or (s[j] == "W" and s[J] == "S"):
            degree -= 90
            continue
    if degree == 360:
        print("CW")
    else:
        print("CCW")