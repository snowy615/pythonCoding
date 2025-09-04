# start = int(input())
# end = int(input())
# total = 0
# for z in range(start, end):
#     z = str(z)
#     y = int(len(z)/2)
#     ha = 0
#     carrot = 0
#     if '2' in z or '3' in z or '4' in z or '5' in z or '7' in z:
#         print(end = '')
#
#     elif '6' in z or '9' in z:
#         if z.count('6') != z.count('9'):
#             carrot = 1
#         for w in range(y):
#             if z[w] != z[-(w + 1)]:
#                 if z[w] == 6 and z[-(w+1)] == 9:
#                     carrot = 1
#                 break
#
#
#
#         if carrot == 0:
#             print(z)
#             total += 1
#
#     else:
#         for x in range(y):
#             if z[x] != z[-(x+1)]:
#                 print(end='')
#                 ha = 1
#                 break
#         if ha == 0:
#             total += 1
#             print(z)
# print(total)
# #
# # 1 100
# # 100 1000
# # 1000 10000
# # 10000 20000
# # 2001 5900
l = [1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1961, 1881, 6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966, 10001, 10101, 10801, 11011, 11111, 11811, 16091, 16191, 16891, 18081, 18181, 18881, 19061, 19161, 19861]
total = 0
start = int(input())
end = int(input())
for z in range(start, end):
    if z in l:
        total += 1
print(total)
# try:
#     if l[z] > start-1 and l[z] < end:
#         total += 1
#         # print(l[z])
#     elif l[z] < start:
#         continue
# except IndexError:
#     break
# elif l[z] < start:
#     continue
# else:
#     break