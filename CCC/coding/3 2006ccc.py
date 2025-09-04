l = []
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
for ha in range(10000):
    word = input()
    time = 0
    if word == 'halt':
        break
    for z in range(len(word)):
        word1 = word[z]
        if word[z] == 'a' or word[z] == 'd' or word[z] == 'g' or word[z] == 'j' or word[z] == 'm' or word[z] == 'p' or word[z] == 't' or word[z] == 'w' or word[z] == '-':
            time += 1
        if word[z] == 'b' or word[z] == 'e' or word[z] == 'h' or word[z] == 'k' or word[z] == 'n' or word[z] == 'q' or word[z] == 'u' or word[z] == 'x':
            time += 2
        if word[z] == 'c' or word[z] == 'f' or word[z] == 'i' or word[z] == 'l' or word[z] == 'o' or word[z] == 'r' or word[z] == 'v' or word[z] == 'y':
            time += 3
        if word[z] == 's' or word[z] == 'z':
            time += 4
    for xx in range(len(word)-1):
        word1 = word[xx]
        word2 = word[xx + 1]
        for i in range(8):
            if word1 in alpha[i] and word2 in alpha[i]:
                time += 2
    l.append(time)
for i in range(len(l)):
    print(l[i])
# print(7)
# w 1
# hi 7
# hotdog 11
# pqrs 16
# xyz 13
# tutu 12
# abracadabra 27
# halt 7
# w
# hi
# hotdog
# pqrs
# xyz
# tutu
# abracadabra
# halt















#
# while True:
#     a = input()
#     if a == "halt":
#         break
#     l.append(a)
#
#
# for i in l:
#     time = 0
#     p = 0
#     for j in i:
#
#         if j == "a" or "d" or "g" or "j" or "m" or "p" or "t" or "w":
#             if p == 1:
#                 time += 2
#             time += 1
#             p = 1
#         if j == "b" or "e" or "h" or "k" or "n" or "q" or "u" or "x":
#             if p == 2:
#                 time += 2
#             time += 2
#             p = 2
#         if j == "c" or "f" or "i" or "l" or "o" or "r" or "v" or "y":
#             if p == 3:
#                 time += 2
#             time += 3
#             p = 3
#         if j == "s" or "z":
#             if p == 4:
#                 time += 2
#             time += 4
#             p = 4
#     print(time)
#     time = 0