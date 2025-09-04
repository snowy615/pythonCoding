hand = []
mapingNotation = [0, 0, 0, '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A', '2']
#number of cards, value

def print_hand():
    for i in range(3):
        print(hand[i], end="  ")
        print()


#player maps to player-1 in hand
def inHandPlay(player, cardNumber, minCard):
    global hand
    print(player, cardNumber, minCard)
    print(len(hand[player]))
    for i in range(len(hand[player])):

        if hand[player][i][1] > minCard and hand[player][i][0] == cardNumber:
            print("in and changed")
            handPlayed = hand[player][i]
            hand[player].pop(i)
            # print(handPlayed)
            return True, handPlayed
    return False, 0


def startPlayer(player):
    print_hand()
    if hand[player] == []:
        return -1
    c = hand[player][0]
    cardIndex = 0
    print(f"player {player}")
    print(f"c {c}")
    for v in range(len(hand[player])):
        print("------")
        print(f"index {v} card deck {hand[player][v]}")
        if hand[player][v][0] > c[0]:
            print("in ")
            c = hand[player][v]
            cardIndex = v

    return cardIndex



def playCards(players, cards):

    n = players
    #get hand into list
    for i in range(n):
        temp = []
        val = []
        h = cards[i].split()
        for j in range(len(h)):
            card = mapingNotation.index(h[j][0])
            if card in val:
                for k in range(len(temp)):
                    if temp[k][1] == card:
                        temp[k][0] += 1
            else:
                temp.append([1, card])
            val.append(card)
        hand.append(temp)
    print_hand()

    #sort
    hand[0].sort()
    hand[1].sort()
    hand[2].sort()
    print_hand()

    playerIndex = 0
    finishedPlayerList = []
    finalOrder = ""
    currentPlayerIndex = 0
    while True:
        if len(finishedPlayerList) == n:
            for j in range(n):
                finalOrder += str(finishedPlayerList[j]) + " "
            return finalOrder
        cardIndex = startPlayer(playerIndex)
        while cardIndex == -1:
            currentPlayerIndex += 1
            cardIndex = startPlayer(playerIndex)
        currentCard = hand[playerIndex][cardIndex][1]
        currentNumber = hand[playerIndex][cardIndex][0]
        currentPlayerIndex += 1
        hand[playerIndex].pop(cardIndex)

        #next player
        play, handPlayed = inHandPlay((currentPlayerIndex+playerIndex)%n, currentNumber, currentCard)
        if play:
            playerIndex = (currentPlayerIndex+playerIndex)%n
            currentPlayerIndex = 1

            for i in range(n):
                if hand[i] == [] and i not in finishedPlayerList:
                    finishedPlayerList.append(i)





playCards(4, ["6S 9C 9H QC 9S 5H KS TC 5C QH JS 5D JH", "3C 7S 5S JD 8H QD TD 2C 6D TS 2D 3S 8D", "TH AC 7H 6H 4D 4H 3D AD 7D 2H 8S 6C 4S", "KC 2S 9D AS 7C KD KH 3H JC 4C QS 8C AH"])

#input
# 3
# JC 6C QD AH 8H TS 5D JD 7D 8D 9C 6H QS 9H 4H KH KS
# 9D 7S JS 2S 8C TC JH 7C TD 4D 6D 4C 5S 3H 2D 3C 6S
# QC 2H AC KC 5H TH KD AD AS 4S 3S 9S 8S 5C 2C QH 3D