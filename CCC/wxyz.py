#
# cnt = 0
# for w in range(-10, 11):
#     for x in range(-10, 11):
#         for y in range(-10, 11):
#             for z in range(-10, 11):
#                 if w == 0 or x == 0 or y == 0 or z == 0:
#                     continue
#                 if x+y+z==w and 1/x+1/y+1/z == 1/w:
#                     print(x, y, z, w)
#                     cnt += 1
# print(cnt)
lis = []
for a in range(-10, 11):
    if a == 0:
        continue
    lis.append([-a,a,a,a])
    lis.append([a, -a, a, a])
    lis.append([-a, a, -a, a])
print(len(lis))
print("\n\n\n\n\n")

for a in range(-10, 11):
    for b in range(-10, 11):
        if a == 0 or b == 0 or a == b or a == -b:
            continue
        lis.append([-b,b,a,a])
        lis.append([-b, a, b, a])
        lis.append([a, -b, b, a])

print(len(lis))
print("\n\n\n\n\n")

cnt = 0
for w in range(-10, 11):
    w_cnt = 0
    for x in range(-10, 11):
        for y in range(-10, 11):
            for z in range(-10, 11):
                if w == 0 or x == 0 or y == 0 or z == 0:
                    continue
                if x+y+z==w and 1/x+1/y+1/z == 1/w:
                    print(x,y,z,w)
                    w_cnt += 1
                    # lis.remove([x,y,z,w])
                    cnt += 1
    print(w_cnt)

print(lis)