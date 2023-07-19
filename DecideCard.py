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
        if toOrder(card1[CARD_NMBR]) - toOrder(card2[CARD_NMBR]) == 2 or toOrder(card2[CARD_NMBR]) - toOrder(card1[CARD_NMBR]) == 2:
            return 1 * mul
        if card1[CARD_NMBR] == '1' and card2[CARD_NMBR] == 'Q' or card2[CARD_NMBR] == '1' and card1[CARD_NMBR] == 'Q':
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
    ind = 0

    if cnt == 0:
        rating = []
        for card in cardsInHand:
            if card[CARD_CLR] == 'W':
                rating.append(100)
                continue
            
            if toValue(card[CARD_NMBR]) < minCard and card[CARD_NMBR] != '1':
                minCard = toValue(card[CARD_NMBR])
                minInd = ind
            
            dbl = 0
            potentialCnt = 0

            for card2 in cardsInHand:
                if card == card2 or card2[CARD_CLR] == 'W':
                    continue
                if card[CARD_CLR] == card2[CARD_CLR] and card[CARD_NMBR] == card2[CARD_NMBR]:
                    dbl += 25
                potentialCnt += compareCards(card, card2, 2)
            
            rating.append(potentialCnt - dbl)
        
        rating[minInd] -= 2

        minCard = 100
        minInd = 0
        ind = 0

        length = len(rating)
        for r in range(0, length):
            if rating[r] < minCard:
                minCard = rating[r]
                minInd = r

        return cardsInHand[minInd]
        
    minCard = 15
    minInd = 0
    ind = 0    

    rating = []
    for unCard in unusedCards:
        if toValue(unCard[CARD_NMBR]) < minCard and unCard[CARD_NMBR] != '1':
            minCard = toValue(unCard[CARD_NMBR])
            minInd = ind

        if unCard[CARD_CLR] == 'W': # Promijenit ako se uvede izbacivanje skupljenog jokera
            rating.append(100)
            continue

        dbl = 0
        potentialCnt = 0

        for card in cardsInHand:
            if unCard == card or card[CARD_CLR] == 'W':
                continue
            if unCard[CARD_CLR] == card[CARD_CLR] and unCard[CARD_NMBR] == card[CARD_NMBR]:
                dbl = 4
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
            potentialCnt += compareCards(unCard, card, -1) # PROVJERIT STA JE UOPCE ZA OCEKIVATI OD OVOGA
        
        rating.append(potentialCnt - dbl)

        for player in game.players:
            for set in player.cardsOnTable:
                for card in set:
                    potentialCnt += compareCards(unCard, card, 1)

        ind += 1

    rating[minInd] -= 2
    ratingInd = rating.index(min(rating))

    return unusedCards[ratingInd]
    