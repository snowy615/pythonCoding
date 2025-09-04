def findMin(word, startIndex, endIndex):
    minl = startIndex
    for i in range(startIndex, endIndex+1):
        if word[i] < word[minl]:
            minl = i
    return minl
def findMax(word, startIndex, endIndex):
    maxn = endIndex
    for i in range(endIndex, startIndex -1, -1):
        if word[i] > word[maxn]:
            maxn = i
    return maxn
def swap(word, a, b):
    temp = word[a]
    word[a] = word[b]
    word[b] = temp

def minfunc(word):
    b_swap = 0
    global start_i, end_i, cnt
    min_i = findMin(word, start_i, end_i)
    while b_swap == 0:
        if b_swap == 1:
            return
        print("min")
        print(f"min_i {min_i}, start_i {start_i}, end_i {end_i}")
        if start_i != min_i:
            print("swap")
            swap(word, start_i, min_i)
            cnt += 1
            b_swap = 1
        if start_i == min_i:
            min_i = findMin(word, start_i+1, end_i)
        start_i += 1
    print(word)
    printLetter(word)
    print("-----")

def maxfunc(word):
    b_swap = 0
    global start_i, end_i, cnt
    print("max")
    max_i = findMax(word, start_i, end_i)
    while b_swap == 0:
        print(f"max_i {max_i}, start_i {start_i}, end_i {end_i}")
        if b_swap == 1:
            return
        if max_i != end_i:
            print("swap")
            swap(word, end_i, max_i)
            b_swap = 1
            cnt += 1
        if max_i == end_i:
            max_i = findMax(word, start_i, end_i-1)
        end_i -= 1

    print(word)
    printLetter(word)
    print("-----")
    print(f"{cnt} cnt")
    print("------")
def printLetter(word):
    for l in word:
        print(chr(l), end = " ")

word = list(input())
for i in range(len(word)-1, -1, -1):
    l = ord(word[i])
    if (l >= ord("A") and l <= ord("Z")) or (l>= ord("a") and l <= ord("z")) or (l>=ord("0") and l<=ord("9")):
        word[i] = ord(word[i])

    else:
        word.pop(i)

print(word)
#-------------------------------
#word is in ascii of letters
start_i = 0
end_i = len(word) -1
min_i = max(word)
max_i = min(word)
cnt = 0
while start_i < end_i:
    minfunc(word)
    if start_i > end_i:
        break
    maxfunc(word)



print(cnt)

