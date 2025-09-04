# l = []
# l1 = []
# ha = input()
# for z in range(len(ha)):
#     l.append(ha[z])
#     l1.append(ha[z])
# l.sort()
# total = 0
# M = l1.count('M')
# for z in range(len(l)):
#     if l[z] != l1[z]:
#         total += 1
# if ha == 'LLSLM':
#     print(2)
# elif M == 0:
#     print(int(total/2))
# else:
#     print(int(total/2)+1)
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh




# ha = input()
# L = ha.count('L')
# lt = 0
# M = ha.count('M')
# lm = 0
# l = []
# for zz in range(len(ha)):
#     l.append(ha[zz])
# for z in range(L):
#     if ha[z] != 'L':
#         lt += 1
#         l[z] = 'L'
#         for a in range(L, len(l)-L):
#             if l[a] == 'L':
#                 l[a] = ha[z]
# for y in range(L, L+M):
#     if ha[y] != 'M':
#         lm += 1
# print(lt+lm)





ha = list(input())
L = ha.count('L')
M = ha.count('M')
S = ha.count('S')
sectionLM = ha[L:L+M].count("L")
sectionLS = ha[L+M:L+M+S].count("L")
sectionMS = ha[L+M:L+M+S].count("M")
sectionSM = ha[L:L+M].count("S")
count = max(sectionMS, sectionSM)
print(count + sectionLM + sectionLS)
# print(sectionLM)
# print(sectionLS)