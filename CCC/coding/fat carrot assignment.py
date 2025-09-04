# from statistics import multimode
# num = int(input())
# l = []
# sum = 0
# for i in range(num):
#     a = int(input())
#     l.append(a)
#     sum += a
# average = sum/num
# print("average = %s" %(average))
# l.sort()
# if num % 2 == 1:
#     print("median = %s" %(l[int((num-1)/2)]))
# else:
#     print("median = %s" %((l[int((num-1)/2)]+l[int((num)/2)])/2))
# s = 0
# ha = 0
# for z in range(num):
#     s += (l[z]-average)**2
#     if l.count(l[z-1]) != l.count(l[z]):
#         ha = 1
# print("方差 = %s"%(s/num))
#
# if ha == 0:
#     print("no mode")
# elif ha == 1:
#     b = multimode(l)
#     print("mode = %s" %(b))

#  assignment 2
# class Solution(object):
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
#         for z in range(len(head)):
#             if head[z] == val:
#                 head[z].remove()
#             else:
#                 head.next
#         return head
#     removeElements([1,2,3,4], 3)


# it = ''
# l = []
# num = 0
# while True:
#     it = input()
#     num += 1
#     if it == 'quit!':
#         break
#     elif len(it) <= 4:
#         l.append(it)
#     elif it[it.index('or')-1] == 'a' or it[it.index('or')-1] == 'e' or it[it.index('or')-1] == 'i' or it[it.index('or')-1] == 'o' or it[it.index('or')-1] == 'u' or it[it.index('or')-1] == 'y':
#         l.append(it)
#     elif it.index('or') + 2 != len(it):
#         l.append(it)
#     else:
#         it = it[:len(it)-2] + 'our'
#         l.append(it)
#
# # print(l)
# for z in range(num-1):
#     print(l[z])
# l = []
# index = 0
# ha = 0
# for i in range(1, 42):
#     l.append(i)
# print(l)
# while len(l)!= 1:
#     lnew = []
#     for z in range(len(l)):
#         if ha == 0 and z%2==0:
#             lnew.append(l[z])
#         elif ha == 1 and z%2 ==1:
#             lnew.append(l[z])
#     if l[-1] == lnew[-1]:
#         ha = 1
#     else:
#         ha = 0
#     l = lnew
#     print(l)
count = 0
for a in range(1, 700):
    for b in range(1, 2021):
        for c in range(1, 2021):
            if a < b < c and a+b+c==0:
                count += 1
print(count)