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
# # print(stepsN)
# # print(stepsB)
# # 4
# # 2
# # 5
# # 3
# # 12
time = 275
if time - int(time/100)*100 > 60:
    print(time - int(time/100)*100)
    b = (time - int(time/100)*100)-60
    time = int(time/100+1)*100 + b
    print(b)
    print(time)