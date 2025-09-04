def p(cards):
    global t_score
    score = 0
    for i in range(len(cards)):
        if cards[i] == "A":
            score += 4
        elif cards[i] == "K":
            score += 3
        elif cards[i] == "Q":
            score += 2
        elif cards[i] == "J":
            score += 1
        print(cards[i], end=" ")
    if len(cards) == 0:
        score += 3
    elif len(cards) == 1:
        score += 2
    elif len(cards) == 2:
        score += 1
    print("         ", end=" ")
    print(score)
    t_score += score
t_score = 0
s = list(input())
print("Cards Dealt               Points")
club = s[s.index("C")+1:s.index("D")]
print("Clubs", end=" ")
p(club)
diamond = s[s.index("D")+1:s.index("H")]
print("Diamonds", end=" ")
p(diamond)
heart = s[s.index("H")+1:s.index("S")]
print("Hearts", end=" ")
p(heart)
spade = s[s.index("S")+1:]
print("Spades", end=" ")
p(spade)
print(f"Total {t_score}")
