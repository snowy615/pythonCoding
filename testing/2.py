l = [7, 9, 7, 14, 15, 8, 20, 11, 18, 18, 17, 11, 17, 7, 8, 19, 8, 11, 19, 17]
for i in l:
    if i%2==0:
        l.append(i)
        l.remove(i)
print(l)
print(20%2)