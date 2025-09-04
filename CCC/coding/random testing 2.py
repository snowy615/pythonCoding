# # # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# b = int(input())
# # # c = int(input())
# # # d = int(input())
# # # for i in range(b):
# # #     print('*'+' '*c+'*'+' '*c+'*')
# # # print('***'+'*'*c*2)
# # # for h in range(d):
# # #     print(' '*(1+c)+'*')
# # # happy = int(input())
# # # if happy > 2:
# # #     print('hello world')
# # #
# # #
# # #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # #
# # # num = 12
# # # print('Hello')
# # # while True:
# # #     if num < 4:
# # #         break
# # #     num -= 2
# # #     print(num)
# #
# # # num = 0
# # # num1 = 0
# # # while True:
# # #     if num1 >= end:
# # #         break
# # #     num1 += 1
# # #     num += num1
# # # print(num)
# # # print('Hello!')
# # # for z in range(10,0,-2):
# # #     print(z)
# # # end = int(input())
# # # num = 0
# # # for z in range(end+1):
# # #     num += z
# # # print(num)
# # # a = 0
# # # print(a)
# # # a = not 1
# # # print(a)
# # # a = not a
# # # print(a)
# #
# # # 1
# # # s = input()
# # # num = s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
# # # print('Number of vowels: %s'%(num))
# #
# # ## 2
# s = input()
# num = 0
# for z in range(len(s)-2):
#     if s[z] == 'b':
#         if s[z+1] == 'o':
#             if s[z+2] == 'b':
#                 num += 1
# print('Number of times bob occurs is: %s'%num)
# #
# # # 3
# num = []
# s = input()
# for z in range(len(s)):
#     total = 1
#     for y in range(z, len(s)-1):
#         if s[y] <= s[y+1]:
#             total += 1
#         else:
#             break
#     num.append(total)
# a = max(num)
# b = num.index(a)
# print(s[b:b+a])
#
# # sorting
# n = int(input())
# l = []
# for z in range(n):
#     num = int(input())
#     l.append(num)
# l.sort()
# for y in range(len(l)):
#     print(l[y])
# # #
# # # alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # # word = input()
# # # total = 0
# # # for z in range(len(word)):
# # #     b = alpha.index(word[z]) + 1
# # #     total += b
# # # print(total)
# #
# #
# #
# #
# #
# # # edx
# # # print('Please think of a number between 0 and 100!')
# # # num = 50
# # # large = 100
# # # small = 0
# # # for z in range(10000):
# # #     print('Is your secret number %s?' % num)
# # #     answer = input()
# # #     print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. %s" % answer)
# # #     if answer == 'c':
# # #         print('Game over. Your secret number was: %s'%num)
# # #         break
# # #     elif answer == 'l':
# # #         large = int((large+num)/2)
# # #         num = large
# # #     elif answer == 'h':
# # #         small = int((small+num)/2)
# # #         num = small
# # #     else:
# # #         print('Sorry, I did not understand your input.')
# #
# # # num = int(input())
# # # for z in range(num):
# # #     word = input()
# # #     word = word.split(':')
# # #     word[0] = int(word[0])
# # # print(word)
# #
# #
# # print('Please think of a number between 0 and 100!')
# # num = 50
# # large = 100
# # small = 0
# # for z in range(10000):
# #     print('Is your secret number %s?' % num)
# #     print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ", end='')
# #     answer = input()
# #     if answer == 'c':
# #         print('Game over. Your secret number was: %s'%num)
# #         # break
# #     elif answer == 'l':
# #         small = num
# #     elif answer == 'h':
# #         large = num
# #     else:
# #         print('Sorry, I did not understand your input.')
# #     num = int((large+small)/2)
#
# # def square(x):
# #     '''
# #     x: int or float.
# #     '''
# #     x *= x
# #     return x
#
# # def iterPower(base, exp):
# #     '''
# #     base: int or float.
# #     exp: int >= 0
# #
# #     returns: int or float, base^exp
# #     '''
# #     num = 1
# #     for z in range(exp):
# #         num *= base
# #         exp -= 1
# #         print(num)
# # time=0
# # alpha = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
# # for i in range(8):
# #     if 'b' in alpha[i] and "a" in alpha[i]:
# #         time+=2
# # print(time)
#
# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
#
#     returns: True if char is in aStr; False otherwise
#     '''
#     small = 0
#     large = len(aStr)
#     # print(small, large, aStr[int((small + large)/2)])
#     if aStr == '':
#         return False
#     if len(aStr) == 1:
#         return aStr == char
#     if char == aStr[int((small + large)/2)]:
#         return True
#     elif char < aStr[int((small + large)/2)]:
#         large = int((small + large)/2)
#         # print(aStr[small:large])
#         return isIn(char, aStr[small:large])
#     elif char > aStr[int((small + large)/2)]:
#         small = int((small + large)/2)
#         # print(aStr[small:large])
#         return isIn(char, aStr[small:large])
# # isIn('g', 'egghilooorstty')
# # print()
# # isIn('r', 'firvvyz')
# # print()
# # isIn('n', 'acffgiijmnqvvwy')
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#

# problem 1
# balance = float(input())
# annualInterestRate = float(input())
# monthlyPaymentRate =float(input())
# Previous_balance = balance
# for z in range(12):
#     Monthly_interest_rate = annualInterestRate / 12.0
#     Minimum_monthly_payment = monthlyPaymentRate * Previous_balance
#     Monthly_unpaid_balance = Previous_balance - Minimum_monthly_payment
#     Updated_balance_month = Monthly_unpaid_balance + Monthly_interest_rate * Monthly_unpaid_balance
#     Updated_balance_month = round(Updated_balance_month, 2)
#     Previous_balance = Updated_balance_month
# print(Updated_balance_month)

# problem 2
# ha = 0
# balance = float(input())
# AnnualInterestRate = float(input())
# MonthlyInterestRate = AnnualInterestRate / 12.0
# for z in range(10, 10000, 10):
#     PreviousBalance = balance
#     for y in range(12):
#         MonthlyUnpaidBalance = PreviousBalance - z
#         PreviousBalance = MonthlyUnpaidBalance + MonthlyInterestRate * MonthlyUnpaidBalance
#         if PreviousBalance <= 0:
#             print(z)
#             ha = 1
#             break
#     if ha == 1:
#         break

# # problem 3
# balance = int(input())
# AnnualInterestRate = float(input())
# MonthlyInterestRate = AnnualInterestRate / 12.0
# low = balance / 12
# high = balance * ((1 + MonthlyInterestRate) ** 12) / 12
# for y in range(1000):
#     PreviousBalance = balance
#     # print(low, high)
#     z = (low + high) / 2
#     for xx in range(12):
#         MonthlyUnpaidBalance = PreviousBalance - z
#         PreviousBalance = MonthlyUnpaidBalance + MonthlyInterestRate * MonthlyUnpaidBalance
#     if high - low <= 0.01:
#         print(round((low+high)/2, 2))
#         break
#     elif PreviousBalance >= 0:
#         low = z
#     elif PreviousBalance < 0:
#         high = z

# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#
#     returns: int, how many values are in the dictionary.
#     '''
#     numk = aDict.keys()
#     numv = aDict.values()
#     total = 0
#     numk = len(numk)
#     numv = list(numv)
#     for z in range(numk):
#         total += len(numv[z])
#     aDict = total
#     return aDict


# def biggest(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#
#     returns: The key with the largest number of values associated with it
#     '''
#     numk = list(aDict.keys())
#     numv = aDict.values()
#     numv = list(numv)
#     f = len(numv[0])
#     s = len(numv[1])
#     if f > s:
#         aDict = numk[0]
#     else:
#         aDict = numk[1]
#     return aDict
# biggest({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]})
# secretWord = 'apple'
# secretWord = list(secretWord)
# secretWord.sort()
# print(secretWord)
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         time = '6:30'
#     print(self.time)
#
# clock = Clock('5:30')
# clock.print_time()

# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self, time):
#         print(time)
#
# clock = Clock('5:30')
# clock.print_time('10:30')

# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         print(self.time)
#
# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()

# ha = {'a': 2, 'b': 3}
# if 'a' in ha.keys():
#     ha['a'] -= 1
# print(ha)


# def calculateHandlen(hand):
#     """
#     Returns the length (number of letters) in the current hand.
#
#     hand: dictionary (string-> int)
#     returns: integer
#     """
#     num = 0
#     fat = list(hand.values())
#     print(fat)
#     for z in range(len(fat)):
#         num += fat[z]
#         print(num)
#     print(num)
#     return num
# calculateHandlen({'e': 1, 'a': 2, 'd': 2, 'g': 1, 'm': 1, 'l': 1})

print((3**200) % 15)