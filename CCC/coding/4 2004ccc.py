#ord(), chr()
shift = list(input())
length = len(shift)
for i in range(length):
    shift[i] = ord(shift[i])
word = list(input())
lis = []
for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        lis.append(word[i])
for i in range(len(lis)):
    num = ord(lis[i])+shift[i%length]-65-64
    num %= 26
    if chr(num +64) == "@":
        print("Z", end="")
    else:
        print(chr(num+64), end="")