word = []
guess = []
green = 0
yellow = 0
for i in range(3):
    a = input()
    for j in range(3):
        word.append(a[j])
for i in range(3):
    a = input()
    for j in range(3):
        guess.append(a[j])
fword = []
fguess = []
for i in range(9):
    if word[i] == guess[i]:
        green += 1
    else:
        fword.append(word[i])
        fguess.append(guess[i])
while len(fguess) != 0:
    if fguess[0] in fword:
        yellow += 1
        fword.remove(fguess[0])
    fguess.remove(fguess[0])
print(green)
print(yellow)