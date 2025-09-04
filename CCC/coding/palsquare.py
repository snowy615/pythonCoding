"""
ID: yansnow2
LANG: PYTHON3
TASK: palsquare
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
fin = open("palsquare.in", "r")
fout = open("palsquare.out", "w")
base = int(fin.readline())
i = 0
while True:
    i+=1
    if i > 300:
        break
    n = isPalindrome(i**2, base)
    if n != False:
        fout.write(f'{exchangebase(i, base)} {n}\n')

