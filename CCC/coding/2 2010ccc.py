# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# s = int(input())
#
# sumN = int(s/(a+b))*(a-b)+(s-(int(s/(a+b)))*(a+b))
# sumB = int(s/(c+d))*(c-d)+(s-(int(s/(c+d)))*(c+d))
# if sumN > sumB:
#     print('Nikky')
# if sumN < sumB:
#     print('Byron')
# if sumN == sumB:
#     print('Tied')
# print(sumN)
# print(sumB)


# version 2
#
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# s = int(input())
# stepsN = int(s/(a+b))*(a-b)
# # print(stepsN)
# if (s-stepsN*(a+b))/a >= 1:
#     x = (s-stepsN) % a
#     x+=stepsN
# elif (s-stepsN)/a < 1:
#     x = (s-stepsN) % a
#     x+=stepsN
# stepsB = int(s/(c+d))*(c-d)
# # print(stepsB)
# if (s-stepsB*(c+d))/c >= 1:
#     x = (s-stepsB) % c
#     x+=stepsB
# elif (s-stepsB)/c < 1:
#     x = (s-stepsB) % c
#     x+=stepsB
#
# if stepsB > stepsN:
#     print('Byron')
# if stepsB < stepsN:
#     print('Nikky')
# if stepsB == stepsN:
#     print('Tied')
#
# version 3

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
turnN = int(s/(a+b))
turnB = int(s/(c+d))
sumN = turnN * (a-b)
sumB = turnB*(c-d)
moduA = s % (a+b)
moduB = s % (c+d)
if moduA == 0:
    sumN += 0
elif moduA < a:
    sumN += moduA
else:
    sumN += 2*a - moduA
# print(sumN)
if moduB == 0:
    sumB += 0
elif moduB < c:
    sumB += moduB
else:
    sumB += 2*c - moduB
# print(sumB)

if sumN > sumB:
    print('Nikky')
if sumN < sumB:
    print('Byron')
if sumN == sumB:
    print('Tied')
# print(sumN)
# print(sumB)




# testing material
# print(stepsN)
# print(stepsB)
# 4
# 2
# 5
# 3
# 12