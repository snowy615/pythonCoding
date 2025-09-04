n = int(input())
barn = input()
lis = []
for i in range(len(barn)):
    for j in range(i+1, len(barn)):
        if barn[j] == "1":
            stall_apart = j-i
            lis.append(j-i)
            i = j
            break
print(lis)
d = min(lis)
print(d)