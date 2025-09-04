def isPrefix(word):
    global start, cnt_i
    if word[:2] == "co" or word[:2] == "de" or word[:2] == "re" or word[:2] == "un":
        start = 2
        cnt_i += 1
    if word[:3] == "dis" or word[:3] == "pre":
        start = 3
        cnt_i += 1

def isSuffix(word):
    global end
    if word[-3:] == "age" or word[-3:] == "ful" or word[-3:] == "ing":
        end -= 3
    if word[-4:] == "less" or word[-4:] == "ment":
        end -= 4


word = input()
start = 0 #starting index after prefix
end = len(word) -1 #ending index before suffix
cnt = 0 #index sum of |

cnt_i = 0 # number of | added in not including suffix

isPrefix(word)
isSuffix(word)
cnt += start
if end != len(word) -1:
    cnt += end+1+cnt_i
print(cnt)
wordlis = []
i = start
while i <= end:
    l = word[i]
    t = 0
    if i < end-1:
        w = word[i:i+2]
        if w == "ch" or w == "ck" or w == "ph" or w == "sh" or w == 'th'or w == "wh" or w == 'wr':
            wordlis.append("C")
            wordlis.append("C")
            t = 1
    if l == "a" or l == "e" or l == "i" or l == "o" or l == 'u':
        wordlis.append("v")
    else:
        if t == 1:
            i += 1
        else:
            wordlis.append("c")
    i += 1
print(wordlis)
#vowel = v, consonant = c, C = combo consonants
i = 1
while i < len(wordlis):
    if wordlis[i] == "c":
        if i < len(wordlis) -1 and wordlis[i-1] == "v" and wordlis[i+1] == "v":
            print(f"i = {i}   c 1 cnt += {start + i + cnt_i}")
            cnt += start + i + cnt_i
            cnt_i += 1
        if (2 < i < len(wordlis) -1 and wordlis[i - 1] == "c" and wordlis[i + 1] == "v" and wordlis[i - 2] == "v") or (3 < i < len(wordlis) -1 and wordlis[i - 1] == "C" and wordlis[i + 1] == "v" and wordlis[i -3] == "v" and wordlis[i - 2] == "C"):
            print(f"i = {i}    c 2 cnt += {start + i + cnt_i}")
            cnt += start + i + cnt_i
            cnt_i += 1
    if wordlis[i] == "C":
        if i + 3 < len(wordlis) and wordlis[i - 1] == "v" and wordlis[i + 2] == "v":
            print(f"i = {i}    C cnt += {start + i + cnt_i}")
            cnt += start + i + cnt_i
            cnt_i += 1
        i += 1
    i += 1

print(cnt)

