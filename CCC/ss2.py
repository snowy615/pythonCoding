s = input()
letter = []
number = []
i = 0
total_sum = 0
while True:
    if len(s) <= i:
        break
    letter.append(s[i])
    i += 1
    # print(letter)
    if ord(s[i]) <= 57:
        num = ""
        while True:
            if len(s) > i and ord(s[i]) <= 57:
                num += s[i]
                i += 1
            else:
                number.append(int(num))
                total_sum += int(num)
                # print(number)
                break
print(letter)
print(number)
print(total_sum)

c = int(input()) % total_sum
# print(c)
i=0
ii = 0
while True:
    if i == len(number):
        print(letter[i-1])
        break
    if ii == c:
        print(letter[i])
        break
    if ii > c:
        print(letter[i-1])
        break
    ii += number[i]
    i += 1





