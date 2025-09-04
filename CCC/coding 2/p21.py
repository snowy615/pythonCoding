#original -> original str
#unused -> unimportant words str
#rows -> str start-end
words = input().split() # input = original
unimportant = input().split() # input = unused
startR, endR = map(int, input().split()) # input = rows

lis = [] #word, cnt, words_before, words_after
punctuation = [".", "?", "!", ",", "/", ":"]

max_word_cnt = 0
max_word_before_cnt = 0
max_word_after_cnt = 0
#need to check if word contains punctutation
for i in range(len(words)):
    if words[i] in unimportant:
        continue
    words_before = []
    cnt = 0
    word_cnt = 0
    before_cnt = 0
    after_cnt = 0
    for j in range(max(i-3,0), i):
        word = words[j]
        #also need to check punctuation
        if word in unimportant:
            break
        elif word[-1] in punctuation:
            break
        else:
            words_before.append(word)
            before_cnt += len(word)+1
            if before_cnt > max_word_before_cnt:
                max_word_before_cnt = before_cnt
    # words_before.reverse()
    words_after = []
    if words[i][-1] in punctuation:
        word_cnt = len(words[i])-1
        cnt += before_cnt + after_cnt + word_cnt
        lis.append([words[i][:-1].lower(), i, words[i][:-1], cnt, words_before, words_after, before_cnt, after_cnt, word_cnt])
    else:
        for j in range(i+1, min(i+4,len(words))):
            word = words[j]

            if word in unimportant:
                break
            elif word[-1] in punctuation:
                words_after.append(word[:-1])
                after_cnt += len(word)
                if after_cnt > max_word_after_cnt:
                    max_word_after_cnt = after_cnt
                break
            else:
                words_after.append(word)
                after_cnt += len(word)
                if after_cnt > max_word_after_cnt:
                    max_word_after_cnt = after_cnt
        word_cnt = len(words[i])
        if len(words[i]) > max_word_cnt:
            max_word_cnt = len(words[i])
        cnt += before_cnt + after_cnt + word_cnt
        lis.append([words[i].lower(), i, words[i], cnt, words_before, words_after, before_cnt, after_cnt, word_cnt])
#lis = words[i].lower(), original index in str, word, cnt, before, after
lis.sort()

for i in lis:
    print(i)


#Need to check punctutation

max_cnt = 0
max_i = 0
for i in range(startR-1, endR):
    if lis[i][3] > max_cnt:
        max_cnt = lis[i][3]
        max_i = i
s = ""
#lis = words[i].lower(), original index in str, 2word, cnt, 4before, after, 6before_cnt, after_cnt, word_cnt
#lis = words[i].lower(), original index in str, word, cnt, before, after
#word, cnt, words_before, words_after
for j in range(max_word_before_cnt-lis[max_i][6]):
    s += "-"

#s += lis[max_i][2]
for j in lis[max_i][4]:
    s += j + " "

s += "<"
s += lis[max_i][2]
for j in range(max_word_cnt-lis[max_i][8]):
    s += "-"
s += "> "
#s += lis[max_i][3]
for j in lis[max_i][5]:
    s += " "+ j

for j in range(max_word_after_cnt-lis[max_i][7]):
    s += "-"
print(s)
print(max_word_before_cnt, max_word_cnt, max_word_after_cnt)