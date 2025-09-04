#ord("a")97
#chr()
word = input()
vowel = ['a', 'e', 'i', 'o', 'u']
vowel_num = [97, 101, 105, 111, 117]

for letter in word:
    print(letter, end="")
    if letter in vowel:
        continue
    num = ord(letter)
    if num > 117:
        print("u", end="")
    else:
        for x in range(len(vowel_num)):
            if num < vowel_num[x]:
                before = num-vowel_num[x-1]
                after = vowel_num[x]-num
                if before > after:
                    print(vowel[x], end="")
                else:
                    print(vowel[x-1], end="")
                break
    if letter == 'z':
        print("z", end="")
    elif chr(num+1) not in vowel:
        print(chr(num+1), end="")
    else:
        print(chr(num+2), end="")
