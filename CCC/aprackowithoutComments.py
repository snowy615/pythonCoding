import copy


def printHand(hand):

    for card in hand:
        print(card, end=" ")


def inOrder(hand):
    """
    checks if the numbers in hand are sorted in increasing order

    args:
        hand (list)

    return:
        boolean: whether the list is sorted. True if it is, false otherwise.
    """
    if hand == sorted(hand):
        return True
    return False


def checkHV(hand):
    """
    calculate the value for hv (heuristic value)
    the heuristic value is defined to be the number of times in the hand that a smaller number is behind a larger number
    ex. 6,3 counts whereas 3,6 or 6,6 does not

    args:
        hand (list)

    return:
        int: hv
    """
    hv = 0
    for i in range(len(hand) - 1):
        if hand[i + 1] < hand[i]:
            hv += 1
    return hv


# return heuristic value + slot
def A(hand, card, handNumber, totalCardNumber):
    hv = -1
    slotRange = int(totalCardNumber / handNumber)
    if totalCardNumber % handNumber != 0:
        slotRange += 1

    cardIndex = int((card - 1) / slotRange)
    ohv = checkHV(hand[max(0, cardIndex - 1): min(handNumber, cardIndex + 2)])
    if slotRange * cardIndex < hand[cardIndex] <= slotRange * (cardIndex + 1):
        return hv, cardIndex

    lis = [card]
    if cardIndex > 0:
        lis.insert(0, hand[cardIndex - 1])
    if cardIndex < handNumber - 1:
        lis.append(hand[cardIndex + 1])

    hv = ohv - checkHV(lis)
    return hv, cardIndex


def B(hand, card):
    hv = -1
    slotIndex = -1
    i = 0

    while True:
        if i + 2 >= len(hand):
            return hv, slotIndex
        if inOrder(hand[i:i + 3]):
            pass
        else:
            for j in range(3):
                newHand = copy.deepcopy(hand)
                newHand[i + j] = card

                if inOrder(newHand[i:i + 3]):
                    ohv = checkHV(hand)
                    hv = ohv - checkHV(newHand)
                    return hv, i + j
        i += 1


def playRackO(info, rack, pile):
    handNumber, totalCardNumber = map(int, info.split())
    hand = list(map(int, rack.split()))
    draw = list(map(int, pile.split()))

    drawIndex = 0
    hv = checkHV(hand)
    print("\nStarting RackO game simulation now!!!\n")

    while True:
        print("\n------------------------------------------------------------")
        print(f"This is card #{drawIndex + 1} with value {draw[drawIndex]}")

        if drawIndex >= len(draw) or inOrder(hand):
            win = False
            if inOrder(hand):
                win = True
            printHand(hand)
            return win, hand

        print("Simulating strategy A")
        Ahv, AslotIndex = A(hand, draw[drawIndex], handNumber, totalCardNumber)
        print(f"The change in heuristic value from A is {Ahv}, at index {AslotIndex} in hand")

        print("Simulating strategy B")
        Bhv, BslotIndex = B(hand, draw[drawIndex])
        print(f"The change in heuristic value from B is:{Bhv}, at index {BslotIndex} in hand")

        print("\nConclusion: ")
        if Ahv == 1 or (Ahv == 0 and Bhv != 1):
            print("Strategy A taken")
            hand[AslotIndex] = draw[drawIndex]
            hv -= Ahv
        elif Bhv != -1:
            print("Strategy B taken")
            hand[BslotIndex] = draw[drawIndex]
            hv -= Bhv
        print("the current hand is: ", end="")
        printHand(hand)
        drawIndex += 1


def main():
    print("Welcome to the game of RackO\n")
    displayRules = input("Would you like to display the rules? (Y/N): ")

    if displayRules == "Y" or displayRules == "y":
        print(
            "The objective of RackO is to sort the hand in increasing order from left to right. \nYou will input your deck to be tested, implementing strategy A and strategy B, through a heuristic approach.")
        print(
            "In this RackO version, there are as many rounds as possible, given that there are still cards in the draw pile and the hand is not in increasing order. The game is won when the objective is achieved. Otherwise, when the cards in the draw pile run out, the game is lost ")
        print(
            "Each round, both methods A and B will be simulated, and the better of the two yielding an optimal heuristic value will be chosen. In the case that the heuristic value is the same, A will be the default choice.")
        print(
            "\nintroducing strategy A:\nstrategy A designates an acceptable interval of numbers in each slot by determining the range of values.\nLooking through the hand from left to right, the function will look for a slot containing a number that fails to be within the acceptable range.\nOnce such a slot is found, function A will be called. The program will attempt to calculate the impact on the heuristic value with card replacement.\nNote: the range of each slot is determined by taking the ceiling of totalCardNumber/totalSlotNumber.\neg. if there was 20 cards, 7 slots, the range would be 1–3, 4-6, 7-9, 10-12, 13-15, 16-18, 19-20 (the last slot contains 2 cards because there are no more available cards)")
        print(
            "\nnow introducing strategy B:\nstrategy B:\nStarting at the front of the hand, continue to find 3 consecutive cards that fails to be in ascending order until either one of the conditions is satisfied:\n1. the replacement of one element in the set of 3 numbers allows for the heuristic value of the hand to improve.\n2. there are no more sets of numbers in the hand to change, strategy B will not be taken.")
        print("Let's start the game by entering information about the deck simulated.")

    info = input(
        "please enter the number of slots in the hand and the largest number in the deck, seperated by a space: ")

    rack = input("please enter the current numbers in the hand, seperated by a space in between each number: ")

    pile = input("please enter numbers in the draw pile, each seperated by a space: ")

    win, hand = playRackO(info, rack, pile)

    print("\nGame over. Your hand is: ", end="")
    printHand(hand)
    if win:
        print("\nCongratulations. You win!")
    else:
        print("\nSorry, you lost.")



main()
