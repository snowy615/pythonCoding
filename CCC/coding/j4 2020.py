word1 = input()
word2 = input()
for z in range(len(word2)):
    if word2[z] not in word1:
        print('no')
        break
    else:

