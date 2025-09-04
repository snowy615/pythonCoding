# count = 0
# for i in range(1002):
#     ha = i
#     for j in range(i+1,1001):
#         ha += j
#         if ha == 2002:
#             count += 1
#             print(i, j)
#             break
#         if ha > 20002:
#             break
# print(count)
count = 0
for i in range(1002):
    ha = i
    for j in range(i+1,1001):
        ha += j
        if ha == 2002:
            count += 1
            print(i, j)
            break
        if ha > 20002:
            break
print(count)