def encodeMessage(text, message):
    punc = "#$%&'()*+,-/:;<=>@[\]^_`{|}~"
    noPuncText = text
    for i in punc:
        print(i)
        noPuncText = noPuncText.replace(i, ' ')
    print(noPuncText)
    sentenceLis = noPuncText.replace('!', '.').replace('?', '.').split('.  ')
    wordLis = []
    for i in range(len(sentenceLis)):
        wordLis.append(sentenceLis[i].split())
    print(wordLis)

    # message encryption
    s = ""
    messageLength = len(message)
    blank = True
    letterCNT = 0
    for i in range(messageLength):
        print(f"i {i}")
        print(f"letter {message[i]}")
        if message[i] == ' ':
            s += "_"
            blank = True
        elif 122 >= ord(message[i]) >= 97 or 65 <= ord(message[i]) <= 90 or 48 <= ord(message[i]) <= 57:
            if not blank:
                s += " "
            letterCNT += 1
            desiredIndex = letterCNT
            while True:
                if desiredIndex <= text.count(message[i]):
                    break
                desiredIndex = int(desiredIndex / 2)
            print(f"desired index {desiredIndex}")
            print(f"total {text.count(message[i])}")
            cnt = 0
            flag = False
            for a in range(len(wordLis)):
                if flag:
                    break
                alen = len(wordLis[a])
                for b in range(alen):
                    if flag:
                        break
                    blen = len(wordLis[a][b])
                    for c in range(blen):
                        if wordLis[a][b][c] == message[i]:
                            cnt += 1
                        if cnt == desiredIndex:
                            s += str(a + 1) + "." + str(b + 1) + "." + str(c + 1)
                            print(str(a + 1) + "." + str(b + 1) + "." + str(c + 1))
                            flag = True
                            blank = False
                            break
            print("----------------")

        else:
            s += message[i]
            blank = True
    print(s)
    return s

encodeMessage("ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League.", "American Computer Science League (ACSL) is fun!")
#encodeMessage("#\" what", "w#")
#encodeMessage("To be or not to be, that is the question - a quote by William Shakespeare.  2B or not 2B - a hexadecimal equivalent!  How would you write it?", "Boolean is always True!")
#encodeMessage("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.  Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure.  We are met on a great battle-field of that war.  We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live.  It is altogether fitting and proper that we should do this.  This was written by Abraham Lincoln on 11/19/1863!", "The #1 speech of all time was less than 8 minutes long!")