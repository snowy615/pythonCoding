def p(lis):
    for i in range(len(lis)):
        print(lis[i], end="")
def findLastBinary(s):
    clis = []
    for i in range(len(s)):
        c = str('%0*d' % (8, int(bin(ord(s[i])).replace("0b", ""))))
        for j in range(len(c)):
            clis.append(c[j])
    p(clis)
    i = 0
    print("-------------")

    while True:
        b_i = list(bin(i).replace("0b", ""))
        l = len(b_i)
        remove = 0
        j = 0
        while True:
            if j > len(clis)-l:
                break
            tf = 1
            for k in range(l):
                # print(f"j {j} k {k}")
                if k>=l or k>=len(clis):
                    tf = 0
                    break
                if clis[k+j] != b_i[k]:
                    tf = 0
                    break
            if tf == 1:
                for k in range(l):
                    clis.pop(j)
                remove = 1
                j -= l
            j+=1

        if remove == 0:
            print(f"i {i}")
            return i-1
        print(f"{b_i} a\n")
        p(clis)
        print()

        i += 1


print(findLastBinary("Roses are red."))