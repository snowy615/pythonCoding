# perfect rhyme: the four lines in the verse all rhyme
# even rhyme: the first two lines rhyme and the last two lines rhyme
# cross rhyme: the first and third lines rhyme, as do the second and fourth
# shell rhyme: the first and fourth lines rhyme, as do the second and third
# free rhyme: any form that is not perfect, even, cross, or shell.
n = int(input())
for i in range(n):
    lis = []
    for z in range(4):
        l = input().lower().split()
        word = l[-1]
        y = len(word)
        while True:
            y -= 1
            if y < 0:
                endword = word
                break
            if word[y] == 'a' or word[y] == 'e' or word[y] == 'i' or word[y] == 'o' or word[y] == 'u':
                endword = word[y:len(word)]
                break
        lis.append(endword)
    if lis[0] == lis[1] == lis[2] == lis[3]:
        print("perfect")
    elif lis[0] == lis[1] and lis[2] == lis[3]:
        print("even")
    elif lis[0] == lis[2] and lis[1] == lis[3]:
        print("cross")
    elif lis[0] == lis[3] and lis[1] == lis[2]:
        print("shell")
    else:
        print("free")