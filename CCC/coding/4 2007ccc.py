word1 = input()
word2 = input()
l1 = []
l2 = []
word1 = word1.split()
word2 = word2.split()
for z in range(len(word1)):
    for y in range(len(word1[z])):
        l1.append((word1[z])[y])
for a in range(len(word2)):
    for b in range(len(word2[a])):
        l2.append((word2[a])[b])
l1.sort()
l2.sort()
if l1 == l2:
    print('Is an anagram.')
else:
    print('Is not an anagram.')
# print(l1)
# print(l2)