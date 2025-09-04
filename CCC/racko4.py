
def inOrder(hand):
    if hand==sorted(hand):
        return True
    return False
def checkHV(lis):
    hv = 0
    for i in range(len(lis)-1):
        if lis[i+1]<lis[i]:
            hv += 1
    return hv
# return heuristic value + slot
def A(hand, card, handNumber, totalCardNumber):
    print(hand)
    print(f"hand, card: {card}, handNumber: {handNumber}, totalCardNumber: {totalCardNumber}")

    hv = -1
    slotIndex = int(totalCardNumber / handNumber)+1
    # cardIndex = hand.index(card)
    cardIndex = int((card-1)/slotIndex)
    print(f"slotIndex {slotIndex} cardIndex: {cardIndex}")
    print(hand[max(0, cardIndex - 1): min(handNumber, cardIndex + 2)])
    ohv = checkHV(hand[max(0, cardIndex - 1): min(handNumber, cardIndex + 2)])
    print(f"ohv: {ohv}")
    print()
    if slotIndex*cardIndex<hand[cardIndex]<=slotIndex*(cardIndex+1):
        return hv, slotIndex
    lis = [card]
    if cardIndex != 0:
        lis.insert(0, hand[cardIndex-1])
    if cardIndex != handNumber-1:
        lis.append(hand[cardIndex+1])
    hv = ohv - checkHV(lis)
    return hv, cardIndex

def B(hand, card):
    hv = -1
    slotIndex = -1

    i = 0
    while True:
        print(f"i {i}")
        if i+2 >= len(hand):
            return hv, slotIndex
        if inOrder(hand[i: i+3])==False:
            print(f"in, {i}")
            print(hand[i: i+3])
            if inOrder([card, hand[i+1], hand[i+2]]):
                print("a")
                ohv = checkHV(hand[max(0, i-1):min(len(hand)-1, i+4)])
                lis = [card, hand[i+1], hand[i+2]]
                if i!=0:
                    lis.insert(0, hand[i-1])
                if i+3 <=len(hand)-1:
                    lis.append(hand[i+3])
                hv = ohv-checkHV(lis)
                return hv, i
            if inOrder([hand[i], card, hand[i+2]]):
                print("b")
                ohv = checkHV(hand[max(0, i-1): min(len(hand)-1, i+4)])
                lis = [hand[i], card, hand[i+2]]
                if i!=0:
                    lis.insert(0, hand[i-1])
                if i+3 <=len(hand)-1:
                    lis.append(hand[i+3])
                hv = ohv-checkHV(lis)
                return hv, i+1
            if inOrder([hand[i], hand[i+1], card]):
                print("c")
                ohv = checkHV(hand[max(0, i-1): min(len(hand)-1, i+4)])
                lis = [hand[i], hand[i+1], card]
                if i!=0:
                    lis.insert(0, hand[i-1])
                if i+3 <=len(hand)-1:
                    lis.append(hand[i+3])
                hv = ohv-checkHV(lis)
                return hv, i+2
        i+=1
def playRackO(info, rack, pile):
    handNumber, totalCardNumber = map(int, info.split())
    hand = list(map(int, rack.split()))
    draw = list(map(int, pile.split()))
    drawIndex = 0
    hv = checkHV(hand)
    print(f"intial hv = {hv}")
    while True:
        print("--------------")
        print(f"drawIndex: {drawIndex}")
        if drawIndex >= len(draw) or inOrder(hand):
            print(hand)
            print("in order")
            result = ""
            for i in range(handNumber):
                result += str(hand[i])+" "
            return result
        print("A")

        Ahv, AslotIndex = A(hand, draw[drawIndex], handNumber, totalCardNumber)
        print(f"Ahv: {Ahv}, AslotIndex {AslotIndex}")
        print("B")
        Bhv, BslotIndex = B(hand, draw[drawIndex])
        print(f"Bhv: {Bhv}, BslotIndex {BslotIndex}")
        if Ahv == 1 or (Ahv==0 and Bhv!=1):
            # A
            print("A taken")
            print(AslotIndex, draw[drawIndex])
            hand[AslotIndex] = draw[drawIndex]
            hv -= Ahv
        elif Bhv != -1:
            # B
            print("B taken")
            hand[BslotIndex] = draw[drawIndex]
            hv -= Bhv
        print(hand)
        drawIndex += 1
#playRackO("9 70","40 35 30 56 32 58 44 17 45","31 37 10 28 21 62 7 64 16 12")
#case wrong
playRackO("15 90","15 12 18 9 28 17 46 51 7 53 65 70 74 84 47","45 73 3 52 54 16 21 44 87 40 68 30 37")
