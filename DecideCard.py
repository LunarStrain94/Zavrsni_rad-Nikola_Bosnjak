from CheckCandidates import *

CARD_CLR = 0
CARD_NMBR = 1

def compareCards(card1, card2, mul):
    if card2[CARD_CLR] == "W":
        return 2 * mul
    if card1[CARD_CLR] == card2[CARD_CLR]:
        if toOrder(card1[CARD_NMBR]) - toOrder(card2[CARD_NMBR]) == 1 or toOrder(card2[CARD_NMBR]) - toOrder(card1[CARD_NMBR]) == 1:
            return 2 * mul
        if card1[CARD_NMBR] == '1' and card2[CARD_NMBR] == 'K' or card2[CARD_NMBR] == '1' and card1[CARD_NMBR] == 'K':
            return 2 * mul
        if (toOrder(card1[CARD_NMBR]) - toOrder(card2[CARD_NMBR]) == 2 or toOrder(card2[CARD_NMBR]) - toOrder(card1[CARD_NMBR]) == 2) and card1[CARD_CLR] == card2[CARD_CLR]:
            return 1 * mul
        if (card1[CARD_NMBR] == '1' and card2[CARD_NMBR] == 'Q' or card2[CARD_NMBR] == '1' and card1[CARD_NMBR] == 'Q') and card1[CARD_CLR] == card2[CARD_CLR]:
            return 1 * mul
    if card1[CARD_NMBR] == card2[CARD_NMBR]:
        if card1[CARD_CLR] != card2[CARD_CLR]:
            return 2 * mul
    return 0


def decideCardToThrowOut(cardsInHand, optimalCards, unusedCards, deck, thrownCards, game):
    comb = combinations(cardsInHand, 5)
    candidates = []
    candidates, cnt = check(comb, candidates)

    minCard = 15
    minInd = 0

    if cnt == 0:
        rating = []
        for card in cardsInHand:
            if card[CARD_CLR] == 'W':
                rating.append(100)
                continue
            
            if toValue(card[CARD_NMBR]) < minCard and card[CARD_NMBR] != '1':
                minCard = toValue(card[CARD_NMBR])
                minInd = cardsInHand.index(card)
            
            dbl = 0
            potentialCnt = 0

            for card2 in cardsInHand:
                if card == card2 or card2[CARD_CLR] == 'W':
                    continue
                if card[CARD_CLR] == card2[CARD_CLR] and card[CARD_NMBR] == card2[CARD_NMBR]:
                    dbl += 15
                potentialCnt += compareCards(card, card2, 2)
            

            rating.append(potentialCnt - dbl)
        
        if minInd < len(rating):
            rating[minInd] -= 2
        elif rating == []:
            pass
        else:
            rating[0] -= 2

        minCard = 100
        minInd = 0

        for r in rating:
            if r < minCard:
                minCard = r
                minInd = rating.index(r)

        if len(cardsInHand) > minInd:
            return cardsInHand[minInd]
        else:
            return cardsInHand[-1]
        
    minCard = 15
    minInd = 0

    rating = []
    for unCard in unusedCards:
        if toValue(unCard[CARD_NMBR]) < minCard and unCard[CARD_NMBR] != '1':
            minCard = toValue(unCard[CARD_NMBR])
            minInd = unusedCards.index(unCard)

        if unCard[CARD_CLR] == 'W':
            rating.append(100)
            continue

        dbl = 0
        potentialCnt = 0

        for card in cardsInHand:
            if unCard == card or card[CARD_CLR] == 'W':
                continue
            if unCard[CARD_CLR] == card[CARD_CLR] and unCard[CARD_NMBR] == card[CARD_NMBR]:
                dbl += 15
                break

        for card in optimalCards:
            if unCard == card or card[CARD_CLR] == 'W':
                continue
            if unCard[CARD_CLR] == card[CARD_CLR] and unCard[CARD_NMBR] == card[CARD_NMBR]:
                continue
            potentialCnt += compareCards(unCard, card, 1)

        for card in unusedCards:
            if unCard == card or card[CARD_CLR] == 'W':
                continue
            if unCard[CARD_CLR] == card[CARD_CLR] and unCard[CARD_NMBR] == card[CARD_NMBR]:
                continue
            potentialCnt += compareCards(unCard, card, 2)

        for card in thrownCards:
            if unCard == card or card[CARD_CLR] == 'W':
                continue
            if unCard[CARD_CLR] == card[CARD_CLR] and unCard[CARD_NMBR] == card[CARD_NMBR]:
                continue
            potentialCnt += compareCards(unCard, card, -1)
        
        for player in game.players:
            for set in player.cardsOnTable:
                for card in set:
                    potentialCnt += compareCards(unCard, card, 1)
        
        rating.append(potentialCnt - dbl)


    if minInd < len(rating):
        rating[minInd] -= 2
    elif rating == []:
        return cardsInHand[-1]
    else:
        rating[0] -= 2

    ratingInd = rating.index(min(rating))

    return unusedCards[ratingInd]
    