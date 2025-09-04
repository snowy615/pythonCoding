
def findLastBinary(s):
    clis = []
    for i in range(len(s)):
        c = str('%0*d' % (8, int(bin(ord(s[i])).replace("0b", ""))))
        for j in range(len(c)):
            clis.append(c[j])
    i = 0

    while True:
        b_i = list(bin(i).replace("0b", ""))
        l = len(b_i)
        remove_1 = 0
        for j in range(len(clis)-l):
            tf = 1
            for k in range(l):
                if clis[k+j] != b_i[k]:
                    tf = 0
                    break
            if tf == 1:
                for k in range(l):
                    clis.pop(j)
                remove_1 = 1
                break

        remove_2 = 0
        for j in range(len(clis)-1, l-1, -1):
            tf = 1
            for k in range(l):
                if k > l or k > j:
                    tf = 0
                    break
                if clis[j-k] != b_i[l-k-1]:
                    tf = 0
                    break
            if tf == 1:
                for k in range(l):
                    clis.pop(j-l+1)
                remove_2 = 1
                break
        if remove_1 == 0 and remove_2 == 0:
            return i-1

        i += 1


print(findLastBinary("Roses are red."))