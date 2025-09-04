alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
vowel = ['a', 'e', 'i', 'o', 'u']
word = []
fword = []
# readrhythem
it = input()
for z in range(len(it)):
    word.append(it[z])
# print(word)
for y in range(len(word)):
    if word[y] == 'a' or word[y] == 'e' or word[y] == 'i' or word[y] == 'o' or word[y] == 'u':
        fword.append(word[y])
    else:
        fword.append(word[y])
        num = alphabet.index(word[y])
        if num <= 2:
            fword.append('a')
            if alphabet[num+1] == 'e':
                fword.append(alphabet[num+2])
            else:
                fword.append(alphabet[num + 1])
        elif num <= 6:
            fword.append('e')
            if alphabet[num+1] == 'i':
                fword.append(alphabet[num+2])
            else:
                fword.append(alphabet[num + 1])
        elif num <= 11:
            fword.append('i')
            if alphabet[num+1] == 'o' or alphabet[num+1] == 'i':
                fword.append(alphabet[num+2])
            else:
                fword.append(alphabet[num + 1])
        elif num <= 17:
            fword.append('o')
            if alphabet[num+1] == 'u' or alphabet[num+1] == 'o':
                fword.append(alphabet[num+2])
            else:
                fword.append(alphabet[num + 1])
        else:
            fword.append('u')
            if alphabet[num] == 'z':
                fword.append('z')
            else:
                if alphabet[num+1] == 'u' or alphabet[num+1] == 'o':
                    fword.append(alphabet[num + 2])
                else:
                    fword.append(alphabet[num + 1])
for a in range(len(fword)):
    print(fword[a], end = '')