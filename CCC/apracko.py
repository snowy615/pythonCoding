import copy


def printHand(hand):
    """
    print the hand with spaces in between each number
    args:
        hand (list)

    no return value
    """
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
    """
    simulate strategy A

    args:
        hand (list) = consist of cards; the cards in hand are desired to be in increasing order
        card (int) = the value of the card that could be added to hand
        handNumber (int) = total number of slots (numbers) in the hand.
        totalCardNumber (int) = the max out of all cards in the deck (both hand and pile)

    return:
        int: hv
    """

    hv = -1  # the heuristic value in this function is initialized to be -1, meaning that no change has happened.

    # calculate the slot range acceptable
    slotRange = int(totalCardNumber / handNumber)
    if totalCardNumber % handNumber != 0:
        slotRange += 1

    # determine the cardIndex, the index where the card should be swapped in the hand.
    cardIndex = int((card - 1) / slotRange)

    # determine the ohv = original heuristic value of hand
    ohv = checkHV(hand[max(0, cardIndex - 1): min(handNumber, cardIndex + 2)])

    # check if the pre-existing card in hand satisfy condition
    if slotRange * cardIndex < hand[cardIndex] <= slotRange * (cardIndex + 1):
        # pre-existing card satisfy the slot range, A should not be taken.
        return hv, cardIndex
    # establish a temporary list lis for simulating a replacement by
    # adding card to the list and the two adjacent cards(if they exist)
    lis = [card]
    if cardIndex > 0:
        lis.insert(0, hand[cardIndex - 1])
    if cardIndex < handNumber - 1:
        lis.append(hand[cardIndex + 1])
    # take the difference of original heuristic value and current value
    hv = ohv - checkHV(lis)
    return hv, cardIndex


def B(hand, card):
    """
        simulate strategy B

        args:
            hand (list)
            card (int)

        return:
            int: hv
        """
    # initalize the heuristic value and slot index to be -1.
    hv = -1
    slotIndex = -1

    # i is the index, used for iterating the hand.
    i = 0

    while True:
        # check if the index has reached the end of the hand
        if i + 2 >= len(hand):
            return hv, slotIndex
        # check if the 3 term sequence of i, i+1, i+2 is in increasing order
        if inOrder(hand[i:i + 3]):
            # in order, move on to iterating the next sequence
            pass
        else:
            # sequence not in order, therefore attempt to replace each of the 3 elements with card
            for j in range(3):
                # create a temporary copy of hand to be changed
                newHand = copy.deepcopy(hand)
                # replace the pre-existing value with card in new hand
                newHand[i + j] = card

                # check if the newHand after replacement is in increasing order
                if inOrder(newHand[i:i + 3]):
                    # in the case that it is, calculate the change in heuristic value by calculating difference
                    # between the original and the updated value
                    ohv = checkHV(hand)
                    hv = ohv - checkHV(newHand)
                    return hv, i + j
        # increase the index by 1, iterating the same procedure for each 3 consecutive elements in hand
        i += 1


def playRackO(info, rack, pile):
    """
    simulate a game of racko based on the parameters of input (info, rack, and pile)
    the ultimate goal of the game is to have a hand consisting of numbers from 1 to n be sorted in increasing order
    Description of racko version:
        - there are as many rounds as needed to either win or end up in a state of no more moves (strategy A and B are both not possible or there are no more cards).
        - In either case, the game will end with win or lose with the steps taken.
        - Each round, out of the two methods (A or B), the better of the two yielding an optimal heuristic value will be chosen
        - if hv is the same, A will be the default choice.


    strategy A:
    strategy A designates an acceptable interval of numbers in each slot by determining the range of values.
        Looking through the hand from left to right, the function will look for a slot containing a number that fails to be within the acceptable range.
        Once such a slot is found, function A will be called. The program will attempt to calculate the impact on the heuristic value with card replacement.

        Note: the range of each slot is determined by taking the ceiling of totalCardNumber/totalSlotNumber.
            eg. if there was 20 cards, 7 slots, the range would be 1–3, 4-6, 7-9, 10-12, 13-15, 16-18, 19-20 (the last slot contains 2 cards because there are no more available cards)

    strategy B:
        Starting at the front of the hand, continue to find 3 consecutive cards that fails to be in ascending order until either one of the conditions is satisfied:
        1. the replacement of one element in the set of 3 numbers allows for the heuristic value of the hand to improve.
        2. there are no more sets of numbers in the hand to change, strategy B will not be taken.


    args:
        info (str): number of slots (var = handNumber) & total number of cards (from 1 to totalCardNumber), seperated by a space
        rack (str): the current numbers in the hand, numbers are seperated by a space
        pile (str): the draw pile of numbers available to be replaced, also the numbers are seperated by a space in between

    return:
        bool: win: status of the game (true=win, false=lose)
        list: hand: hand at the end of the game
    """
    # establishing the indiviudal elements (e.g. handNumber) by breaking down the input information
    handNumber, totalCardNumber = map(int, info.split())
    hand = list(map(int, rack.split()))
    draw = list(map(int, pile.split()))

    # initalize drawIndex and the heuristic value
    drawIndex = 0  # draw index is the index for the draw (list)
    hv = checkHV(hand)

    print("\nStarting RackO game simulation now!!!\n")

    # start the RackO game
    while True:
        print("\n------------------------------------------------------------")
        print(f"This is card #{drawIndex + 1} with value {draw[drawIndex]}")

        # game over when there are no more cards or the cards are in order
        if drawIndex >= len(draw) or inOrder(hand):
            # check result of the game
            win = False
            if inOrder(hand):
                win = True

            printHand(hand)
            return win, hand

        # strategy A
        print("Simulating strategy A")
        Ahv, AslotIndex = A(hand, draw[drawIndex], handNumber, totalCardNumber)
        print(f"The change in heuristic value from A is {Ahv}, at index {AslotIndex} in hand")

        # strategy B
        print("Simulating strategy B")
        Bhv, BslotIndex = B(hand, draw[drawIndex])
        print(f"The change in heuristic value from B is:{Bhv}, at index {BslotIndex} in hand")

        print("\nConclusion: ")
        # evaluate which strategy is better based on the improvement of heuristic value.
        # If hv value is equal, A should be taken.
        # values of -1 should not be taken.
        # under each condition, hand and heuristic value will be updated accordingly
        if Ahv == 1 or (Ahv == 0 and Bhv != 1):
            # A
            print("Strategy A taken")
            hand[AslotIndex] = draw[drawIndex]
            hv -= Ahv
        elif Bhv != -1:
            # B
            print("Strategy B taken")
            hand[BslotIndex] = draw[drawIndex]
            hv -= Bhv
        print("the current hand is: ", end="")
        printHand(hand)
        drawIndex += 1


def main():
    print("Welcome to the game of RackO\n")
    # ask the player if they want to see the rules by allowing them to input yes or no.
    displayRules = input("Would you like to display the rules? (Y/N): ")

    # if yes, display the rules
    if displayRules == "Y" or displayRules == "y":
        print("The objective of RackO is to sort the hand in increasing order from left to right. ")

    # ask player to input on 3 lines:
    # 1. number of slots (var = handNumber) & total number of cards (from 1 to totalCardNumber), seperated by a space
    info = input(
        "please enter the number of slots in the hand and the largest number in the deck, seperated by a space: ")
    # 2. the current numbers in the hand, numbers are seperated by a space
    rack = input("please enter the current numbers in the hand, seperated by a space in between each number: ")
    # 3. the draw pile of numbers available to be replaced, also the numbers are seperated by a space in between
    pile = input("please enter numbers in the draw pile, each seperated by a space: ")

    # call playRackO function
    win, hand = playRackO(info, rack, pile)

    print("\nGame over. Your hand is: ", end="")
    printHand(hand)
    if win:
        print("\nCongratulations. You win!")
    else:
        print("\nSorry, you lost.")



# 9 70
# 40 35 30 56 32 58 44 17 45
# 31 37 10 28 21 62 7 64 16 12
main()
