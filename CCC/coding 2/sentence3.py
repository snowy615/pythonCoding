# N C V J B P A(a, an) T(the)
dic = ["A", ["a"], 0, "T", ["the"], 0]
vowel = ["a", "e", "i", "o", "u"]
n = int(input())
for i in range(n):
    t = input().split()
    dic.append(t[0])
    t.pop(0)
    dic.append(t)
    dic.append(0)
print(dic)
sentence_lis = input().split()
for s in sentence_lis:
    #word = sentence
    word = ""
    if s[0] == "Q":
        word += "What "
    for l in range(1, len(s)):
        index = dic.index(s[l])+1
        #index -> dic index
        if l == 1 and s[0] != "Q":
            word += dic[index][dic[index+1]].capitalize()

            if dic[index][dic[index+1]] == "a" and dic[dic.index(s[l+1])+1][dic[dic.index(s[l+1])+2]][0] in vowel:
                word += "n"
        else:
            word += dic[index][dic[index+1]]
            if dic[index][dic[index+1]] == "a" and dic[dic.index(s[l+1])+1][dic[dic.index(s[l+1])+2]][0] in vowel:
                word += "n"
        dic[index+1] += 1
        dic[index + 1] %= len(dic[index])
        if l != len(s)-1:
            word += " "
    if s[0] == "D" or s[0] == "I":
        word += "."
    if s[0] == "Q":
        word += "?"
    if s[0] == "E":
        word += "!"
    print(word)
    print("----------")