from CheckCandidates import *

CARD_CLR = 0
CARD_NMBR = 1

def isCompatible(can, available):
    possible = True
    for card in can:
        if card not in available:
            possible = False
            break
    return possible



def updateAvailableCards(can, av):
    available = av.copy()
    i = 0
    while i < len(available):
        if available[i] in can:
            available.pop(i)
            continue
        i += 1
    return available



def finalEval(stats): #[cnt, sum, jokerCount, flushCount]
    final = []
    for stat in stats:
        final.append(stat[0] + stat[1] - stat[2] + stat[3])
    return final



def miniEval(can, cnt, sum, jokerCount, flushCount):
    if can[0][CARD_CLR] == can[1][CARD_CLR] or can[0][CARD_CLR] == can[2][CARD_CLR]:
        flushCount += 1
    i = 0
    while i < len(can):
        if can[i][CARD_NMBR] == "W":
            jokerCount += 1
        if can[i][CARD_NMBR] != "W":
            sum += toValue(can[i][CARD_NMBR])
        elif can[i][CARD_NMBR] == "W" and i > 0:
            if toValue(can[i-1][CARD_NMBR]) < 9 and len(can) > 2 and i > 1:
                if toValue(can[i-1][CARD_NMBR]) == toValue(can[i-2][CARD_NMBR]):
                    sum += toValue(can[i-1][CARD_NMBR])
                else:
                    sum += toValue(can[i-1][CARD_NMBR]) + 1
            elif toValue(can[i-1][CARD_NMBR]) < 9:
                sum += toValue(can[i-1][CARD_NMBR]) + 1
            else:
                sum += 10
        i += 1
        cnt += 1
    return cnt, sum, jokerCount, flushCount



def evaluateCandidateSumStraightFlush(candidates):
    length = len(candidates)
    jokerCount = 0
    numbers = []
    colors = []
    for card in candidates:
        if card[CARD_NMBR] == "W":
            jokerCount += 1
            numbers.append("W")
            colors.append("W")
        elif card[CARD_NMBR] == "1":
            if candidates.index(card) == 0:
                numbers.append(1)
                colors.append(card[CARD_CLR])
            else:
                numbers.append(14)
                colors.append(card[CARD_CLR])
        else:
            numbers.append(toOrder(card[CARD_NMBR]))
            colors.append(card[CARD_CLR])

    sumCandidates = 0

    i = 0
    while "W" in numbers:
        if numbers[i] == "W":
            if i == 0:
                if numbers[i + 1] != "W":
                    numbers[i] = numbers[i + 1] - 1
                    colors[i] = colors[i + 1]
            elif i == length - 1:
                if numbers[i - 1] != "W":
                    numbers[i] = numbers[i - 1] + 1
                    colors[i] = colors[i - 1]
            else:
                if numbers[i - 1] != "W":
                    numbers[i] = numbers[i - 1] + 1
                    colors[i] = colors[i - 1]
                elif numbers[i + 1] != "W":
                    numbers[i] = numbers[i + 1] - 1
                    colors[i] = colors[i + 1]
        
        if i < length - 1:
            i += 1
        else:
            i = 0
    
    for num in numbers:
        if num == 1:
            sumCandidates += 10
        elif num < 10:
            sumCandidates += num
        else:
            sumCandidates += 10
    
    return sumCandidates



def evaluateCandidateSumFlush(candidates):
    num = 0
    for can in candidates:
        if can[CARD_NMBR] != "W":
            num = toOrder(can[CARD_NMBR])    
            break
    if num > 9:
        num = 10
    if num == 1:
        num = 10
    return len(candidates) * num



def takeOutRedundantCombos(combos, stats):
    i = 0
    while i < len(combos):
        if len(combos[i]) < 2:
            i += 1
            continue
        j = 0
        while j < len(combos):
            if len(combos[i]) != len(combos[j]) or i == j:
                j += 1
                continue
            if len(combos[i]) == 2:
                if combos[j][0] in combos[i] and combos[j][1] in combos[i]:
                    combos.pop(j)
                    stats.pop(j)
                    continue
            if len(combos[i]) == 3:
                if combos[j][0] in combos[i] and combos[j][1] in combos[i] and combos[j][2] in combos[i]:
                    combos.pop(j)
                    stats.pop(j)
                    continue
            if len(combos[i]) == 4:
                if combos[j][0] in combos[i] and combos[j][1] in combos[i] and combos[j][2] in combos[i] and combos[j][3] in combos[i]:
                    combos.pop(j)
                    stats.pop(j)
                    continue
            j += 1
        i += 1
    return combos, stats


def evaluation(candidates, cardsToCheck):
    combos = []
    stats = []

    for can in candidates: # evaluacija jedinica i dodavanje stats i combos
        cnt, sum, jokerCount, flushCount = 0, 0, 0, 0
        cnt, sum, jokerCount, flushCount = miniEval(can, cnt, sum, jokerCount, flushCount)
        combos.append([can])
        stats.append([cnt, sum, jokerCount, flushCount])

    doubles = [] # spajanje dvojki
    for can in candidates:
        available = updateAvailableCards(can, cardsToCheck)
        for can2 in candidates:
            if can == can2:
                continue
            if isCompatible(can2, available):
                doubles.append([can, can2])
    
    if doubles == []: # ako nema dvojki
        combos, stats = takeOutRedundantCombos(combos, stats)
        return combos, stats

    i = 0
    while i < len(doubles): # oduzimanje redundantnih jedinica od dvojki
        j = 0
        while j < len(combos):
            if combos[j][0] == doubles[i][0] or combos[j][0] == doubles[i][1]:
                combos.pop(j)
                stats.pop(j)
                continue
            j += 1
        i += 1
    
    for dbl in doubles: # evaluacija dvojki i dodavanje stats i combos
        cnt, sum, jokerCount, flushCount = 0, 0, 0, 0
        cnt, sum, jokerCount, flushCount = miniEval(dbl[0], cnt, sum, jokerCount, flushCount)
        cnt, sum, jokerCount, flushCount = miniEval(dbl[1], cnt, sum, jokerCount, flushCount)
        combos.append(dbl)
        stats.append([cnt, sum, jokerCount, flushCount])

    triples = [] 
    for dbl in doubles: # spajanje trojki
        for can in candidates:
            if can in dbl:
                continue
            available = updateAvailableCards(can, cardsToCheck)
            if isCompatible(dbl[0], available):
                available = updateAvailableCards(dbl[0], available)
                if isCompatible(dbl[1], available):
                    triples.append([dbl[0], dbl[1], can])
    
    if triples == []: # ako nema trojki
        combos, stats = takeOutRedundantCombos(combos, stats)
        return combos, stats

    i = 0
    while i < len(triples): # oduzimanje redundantnih dvojki od trojki
        j = 0
        while j < len(combos):
            if len(combos[j]) > 1:
                if combos[j][0] == triples[i][0] and combos[j][1] == triples[i][1]:
                    combos.pop(j)
                    stats.pop(j)
                    continue
            j += 1
        i += 1

    for trio in triples: # evaluacija trojki i dodavanje combos i stats       
        cnt, sum, jokerCount, flushCount = 0, 0, 0, 0
        cnt, sum, jokerCount, flushCount = miniEval(trio[0], cnt, sum, jokerCount, flushCount)
        cnt, sum, jokerCount, flushCount = miniEval(trio[1], cnt, sum, jokerCount, flushCount)
        cnt, sum, jokerCount, flushCount = miniEval(trio[2], cnt, sum, jokerCount, flushCount)
        combos.append(trio)
        stats.append([cnt, sum, jokerCount, flushCount])

    quadruples = []
    for can in candidates: # spajanje cetvorki
        for trio in triples:
            if can in trio:
                continue
            available = updateAvailableCards(can, cardsToCheck)
            if isCompatible(trio[0], available):
                available = updateAvailableCards(trio[0], available)
                if isCompatible(trio[1], available):
                    available = updateAvailableCards(trio[1], available)
                    if isCompatible(trio[2], available):
                        quadruples.append([can, trio[0], trio[1], trio[2]])

    if quadruples == []: # ako nema cetvorki
        combos, stats = takeOutRedundantCombos(combos, stats)
        return combos, stats

    i = 0
    while i < len(quadruples): # oduzimanje redundantnih trojki od cetvorki
        j = 0
        while j < len(combos):
            if len(combos[j]) > 2:
                if quadruples[i][0] == combos[j][0] and quadruples[i][1] == combos[j][1] and quadruples[i][2] == combos[j][2]:
                    combos.pop(j)
                    stats.pop(j)
                    continue
            j += 1
        i += 1
    
    for quad in quadruples: # evaluacija cetvorki i dodavanje combos i stats       
        cnt, sum, jokerCount, flushCount = 0, 0, 0, 0
        cnt, sum, jokerCount, flushCount = miniEval(quad[0], cnt, sum, jokerCount, flushCount)
        cnt, sum, jokerCount, flushCount = miniEval(quad[1], cnt, sum, jokerCount, flushCount)
        cnt, sum, jokerCount, flushCount = miniEval(quad[2], cnt, sum, jokerCount, flushCount)
        cnt, sum, jokerCount, flushCount = miniEval(quad[3], cnt, sum, jokerCount, flushCount)
        combos.append(quad)
        stats.append([cnt, sum, jokerCount, flushCount])

    combos, stats = takeOutRedundantCombos(combos, stats)
    return combos, stats