# a_list = ["a", "b", "c"]
# order = [1, 0, 2]
#
# # a_list = [a_list[z] for z in order]
# #
# # print(a_list)
# # for i in range(3):
# #     print(i)
# # ha = 'haha'
# # print(len(ha))
# word = input()
# # z = [['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P', 'Q', 'R'], ['S', 'T', 'U', 'V', 'W', 'X'], ['Y', 'Z', ' ', '-', '.', 'enter']]
# print(word[2])
# # print(len(word))
# a = input()
# a = a[:1] + 'b' + a[:-(len(a)-1)]
# # print(a)
# l = []
# it = input()
# it = it[:len(it) - it.index('or') + 1] + 'our'
# l.append(it)
# print(l)
# # print(it.index('or'))
# z = 22
# z = str(z)
# if any(map(str.isdigit('2'), z)) == True or any(map(str.isdigit, z)) == True:
#     print('ha')
# s = "abc1"
# contains_digit = any(map(str.isdigit, s))
#
# print(contains_digit)


# numbers = [2349523234, 12345123, 12346671, 13246457, 134123431]
#
# for number in numbers:
#     if (4 in number):
#         print(number + "True")
#     else:
#         print("False")

# def isDigitPresent(x, d):
#     # Breal loop if d is present as digit
#     while (x > 0):
#
#         if (x % 10 == d):
#             break
#
#         x = x / 10
#
#     # If loop broke
#     return (x > 0)
#
#
# # function to display the values
# def printNumbers(n, d):
#     for i in range(0, n + 1):
#         if (i == d or isDigitPresent(i, d)):
#             print(i, end=" ")
#
#
# n = 47
# d = 7
# print("The number of values are")
# # printNumbers(n, d)
# for n in range(1, 500):
# # r = m % n
# #     if r == 0:
# #         s = 0
# #     else:
# #         s = n % r
#     if s == 0:
#         t = 0
#     else:
#         t = r % s
#     if r >= 1 and r <= 15 and s >= 2 and s <= 9 and t == 0:
#         print(n)
# #         total += 1
# # print(total)
# m = 500
# total = 0
# #
#
#
# for z in range(9):
#     for y in range(9):
#         if (z*10000+200+10*y+1) % 99 == 16:
#             print(z*10000+200+10*y+1)
#             break

# for w in range(10):
#     if w != 6 and w != 9:
#         carrot = 1
#         print(w)



def rotate():
    m = int(input())
    n = int(input())
    counter = 0
    for i in range(m, n+1, 1):
        if i in [1, 8]:
            counter += 1
        elif i in [11, 69, 88, 96]:
            counter += 1
        elif i in [101,111,181,609,619,689,808,818,888,906,916,986]:
            counter += 1
        elif i in [1001,1111,1691,1961,1881,6009,6119,6699,6889,6969,8008,8118,8698,8888,8968,9006,9116,9696,9886,9966]:
            counter += 1
        elif i in [10001,10101,10801,11011,11111,11811,16091,16191,16891,18081,18181,18881,19061,19161,19861]:
            counter += 1
    print(counter)


rotate()