"""
ID: yansnow2
LANG: PYTHON3
TASK: dualpal
"""
def isPalindrome(n, base):
    n = exchangebase(n, base)
    i = -1
    j = len(n)
    while True:
        if i >= j:
            break
        i+=1
        j-=1
        if n[i] != n[j]:
            return False
    return n
def exchangebase(i, base):
    lis = []
    quo = int(i / base)
    remainder = i % base
    while True:
        if quo == 0:
            break
        lis.append(remainder)
        remainder = quo % base
        quo = int(quo / base)
    lis.append(remainder)
    lis.reverse()
    num = ""
    for i in lis:
        if i >= 10:
            i = chr(i + 55)
        num += str(i)
    return num
fin = open("dualpal.in", "r")
fout = open("dualpal.out", "w")
lis = list(map(int, fin.readline().split()))
N = lis[0]
S = lis[1]
count = 0
while True:
    c = 0
    if count >= N:
        break
    S += 1
    for i in range(2, 11):
        if isPalindrome(S, i) != False:
            c+=1
    if c >= 2:
        count += 1
        fout.write(f"{S}\n")
