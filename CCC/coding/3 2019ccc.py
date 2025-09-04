# num = input()
# num = num.split()
# total = 0
# for z in range(len(num)-1):
#     if num[z] == num[z+1]:
#         total += 1
# # print(num)
# # print(total)
num = int(input())
fl = []
for z in range(num):
    text = input()
    l = []
    total = 1
    # for y in range(len(text)):
    #     l.append(text[y])
    for y in range(1, len(text)):
        if text[y] == text[y-1]:
            total += 1
        else:
            fl.append(total)
            fl.append(' ')
            fl.append(text[y-1])
            fl.append(' ')
            total = 1
    fl.append(total)
    fl.append(' ')
    fl.append(text[y])
    fl.append(',')
for a in range(len(fl)):
    if fl[a] != ',':
        print(fl[a], end='')
    else:
        print('')
# print(l)