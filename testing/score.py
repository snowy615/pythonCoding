def score(text, speak):
    s1 = text.split()
    s2 = speak.split()
    wrong = []
    c = 0
    w = 0
    for i in range(len(s2)):
        c_w = 0
        if i < 5:
            s = 0
        else:
            s = i-5
        for j in range(s, min(i+5, len(s1))):
            if s2[i] == s1[j]:
                c += 1
                c_w = 1
                break
        if c_w == 0:
            wrong.append(s2[i])
            w += 1
    print(c/(c+w))
    print(wrong)

score("hello fat carrot", "yes sir fat carrot")