cowalphabet = list(input())
word = input()
count_num = 1
for i in range(1, len(word)):
    if cowalphabet.index(word[i]) > cowalphabet.index(word[i-1]):
        continue
    count_num += 1
print(count_num)