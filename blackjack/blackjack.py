import random

def openCSV():
    faceList = []
    valueList = []
    fname = 'deck.csv'
    dataFile = open(fname, 'r')
    dataFile.readline()
    for line in dataFile:
        line = line.strip()
        face, value = line.split(',')
        faceList.append(face)
        valueList.append(value)
    dataFile.close()
    return faceList, valueList


def getDealerHand(valueList):
    dealerHand = 0
    aceCount = 0

    while dealerHand < 17:
        card = int(random.choice(valueList))
        dealerHand += card
        if card == 11:
            aceCount += 1

        while dealerHand > 21 and aceCount > 0:
            dealerHand -= 10
            aceCount -= 1

    return dealerHand


def getPlayerHand(valueList):
    aceCount = 0
    firstCard = int(random.choice(valueList))
    secondCard = int(random.choice(valueList))
    hand = firstCard + secondCard
    if firstCard == 11:
        aceCount += 1
    if secondCard == 11:
        aceCount += 1

    if hand == 22:
        hand = 12
        aceCount = 1

    print(f"Your starting hand: {firstCard}, {secondCard} (Total: {hand})")

    while hand < 21:
        choice = input("Enter choice [H for hit, S for stand]: ").lower()
        if choice == 's':
            break
        elif choice == 'h':
            newCard = int(random.choice(valueList))
            print(f"You drew: {newCard}")
            hand += newCard
            if newCard == 11:
                aceCount += 1

            while hand > 21 and aceCount > 0:
                hand -= 10
                aceCount -= 1
            print(f"Your total is now: {hand}")
        else:
            print("Invalid input. Please choose H or S.")

    return hand


def determineWinner(playerTotal, dealerTotal):
    if playerTotal > 21:
        return 'lose'
    elif dealerTotal > 21:
        return 'win'
    elif playerTotal > dealerTotal:
        return 'win'
    elif playerTotal < dealerTotal:
        return 'lose'
    else:
        return 'push'  # tie


def main():
    faceList, valueList = openCSV()

    try:
        bet = float(input("Enter your bet amount per round: "))
        rounds = int(input("Enter how many rounds to simulate: "))
    except ValueError:
        print("Invalid input.")
        return

    balance = 0

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")
        dealerFirstCard = int(random.choice(valueList))
        print(f"The dealer shows: {dealerFirstCard}")
        dealerTotal = getDealerHand(valueList)
        playerTotal = getPlayerHand(valueList)
        print(f"Dealer's final hand: {dealerTotal}")
        print(f"Your final hand: {playerTotal}")

        result = determineWinner(playerTotal, dealerTotal)

        if result == 'win':
            balance += bet
            print(f"You win ${bet}!")
        elif result == 'lose':
            balance -= bet
            print(f"You lose ${bet}.")
        else:
            print("Push. No money won or lost.")

    if balance > 0:
        print(f"\nYou won a total of ${balance}")
    elif balance < 0:
        print(f"\nYou lost a total of ${-balance}")
    else:
        print("\nYou broke even.")

if __name__ == "__main__":
    main()
