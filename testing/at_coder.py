s = input()
cnt = 0
if s == "0":
    pass
else:
    i = 0
    n = len(s)
    while i < n:
        print(f"i {i}")
        cnt += 1
        if i < n-1:
            if s[i] == "0" and s[i+1] == "0":
                i += 1
        print(f"cnt {cnt}")
        i += 1

print(cnt)