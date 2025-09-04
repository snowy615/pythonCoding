def find(letter, target, isUsed):
    for i in range(5):
        if target[i] == letter:
            if isUsed[i] == False:
                return i
    return 5
lis = [] #G, Y, first, last, vowel, word
notUsed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = input().split()
target = x[0]
x.pop(0)
for i in x:
    G = 0
    Y = 0
    vowel = 0
    isUsed = [False, False, False, False, False]
    for j in range(5):
        if i[j] in notUsed:
            notUsed.remove(i[j])
        if target[j] == i[j]:
            G += 1
            isUsed[j] = True
            if target[j] == 'a' or target[j] == 'e' or target[j] == 'i' or target[j] == 'o' or target[j] == 'u':
                vowel += 1
    for j in range(5):
        if find(i[j], target, isUsed) != 5 and target[j] != i[j]:
            index_of_the_thing = find(i[j], target, isUsed)
            print(f"index {index_of_the_thing}, i {i}, j {j}, letter {i[j]}, isUsed {isUsed}")
            isUsed[index_of_the_thing] = True
            Y += 1
    if G > 0 or Y > 0:
        if target[0] == i[0]:
            first = 1
        else:
            first = 0
        if target[-1] == i[-1]:
            last = 1
        else:
            last = 0
        lis.append([G, Y, first, last, vowel, i])
lis.sort(reverse=True)
for j in lis:
    print(j)


print("-------------------------")
if len(lis) >= 6:
    for i in range(6):
        print(lis[i][5] + " ", end="")
else:
    for i in notUsed:
        print(i, end="")

