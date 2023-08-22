from itertools import combinations

CARD_CLR = 0
CARD_NMBR = 1

def toOrder(ch):
    if ch == "J":
        return 11
    if ch == "Q":
        return 12
    if ch == "K":
        return 13
    if ch == "W":
        return 25
    return int(ch) 

def toValue(ch):
    if ch == "J":
        return 10
    if ch == "Q":
        return 10
    if ch == "K":
        return 10
    if ch == "1":
        return 10
    return int(ch)


def sortCards(candidates):
    candidates = sorted(candidates)
    while len(candidates) < 5:
        candidates.append(("PLACEH", "0", "LDER"))
    j = 0
    while j < 4:
        if candidates[j][CARD_CLR] == "W":
            candidates.append(candidates[j])
        j += 1

    while j > -1:
        if candidates[j][CARD_CLR] == "W":
            candidates.pop(j)
        j -= 1

    for i in range(0, len(candidates)-1):
        if toOrder(candidates[i+1][CARD_NMBR]) < toOrder(candidates[i][CARD_NMBR]) and candidates[i+1][CARD_CLR] == candidates[i][CARD_CLR]:
            tmp = candidates[i]
            candidates[i] = candidates[i+1]
            candidates[i+1] = tmp
    return candidates



def candidateFlush(candidates):
    candidates = sortCards(candidates)
    while len(candidates) < 5:
        candidates.append(("PLACEH", "0", "LDER"))
    for i in range(0, 5):
        tmp = [candidates[i]]
        for j in range(0, 5):
            if i == j:
                continue
            elif candidates[j][CARD_CLR] == "W" or (candidates[j][CARD_CLR] != tmp[-1][CARD_CLR] and candidates[j][CARD_NMBR] == tmp[0][CARD_NMBR]):
                possible = True
                for k in range(0, len(tmp)):
                    if candidates[j][CARD_CLR] == tmp[k][CARD_CLR] and candidates[j][CARD_NMBR] == tmp[k][CARD_NMBR]:
                        possible = False
                        break
                if possible:    
                    tmp.append(candidates[j])
            if len(tmp) == 4:
                return tmp
        if len(tmp) > 2:
            return tmp
    return False



def candidateStraightFlush(candidates):
    if len(candidates) < 2:
        return False
    candidates = sortCards(candidates)
    while len(candidates) < 5:
        candidates.append(("PLACEH", "0", "LDER"))
    for i in range(0, 5):
        if candidates[i][CARD_CLR] == "W":
            continue
        tmp = [candidates[i]]
        j = 0
        while j < 5:
            if len(tmp) == 2:
                if tmp[0][CARD_NMBR] == "K" and tmp[1][CARD_NMBR] == "A":
                    for can in candidates:
                        if can[CARD_CLR] == "W":
                            tmp.insert(0, can)
                            return tmp
            if tmp[-1][CARD_CLR] == 'W' and toOrder(candidates[j][CARD_NMBR]) - toOrder(tmp[-2][CARD_NMBR]) == 2 and candidates[j][CARD_CLR] == tmp[0][CARD_CLR]:
                tmp.append(candidates[j])
                j = 0
                continue
            if tmp[-1][CARD_CLR] == 'W' and candidates[j][CARD_NMBR] == "1" and tmp[-2][CARD_NMBR] == "Q" and candidates[j][CARD_CLR] == tmp[0][CARD_CLR]:
                tmp.append(candidates[j])
                j = 0
                continue
            if candidates[j][CARD_CLR] == "W" and candidates[j] not in tmp:
                taken = False
                for k in tmp:
                    if k[1] == "W":
                        taken = True
                if len(tmp) > 1 and tmp[-2][CARD_NMBR] == "K" or taken == True:
                    j += 1
                    continue  
                tmp.append(candidates[j])
                j = 0
                continue
            if candidates[j][CARD_NMBR] == "1" and tmp[-1][CARD_NMBR] == "K" and candidates[j][CARD_CLR] == tmp[0][CARD_CLR]:
                tmp.append(candidates[j])
                j = 0
                continue
            if tmp[-1][CARD_NMBR] != "W" and candidates[j][CARD_CLR] == tmp[0][CARD_CLR] and toOrder(candidates[j][CARD_NMBR]) - toOrder(tmp[-1][CARD_NMBR]) == 1 and candidates[j] not in tmp:
                if len(tmp) > 1 and tmp[-2][CARD_NMBR] == "K":
                    j += 1
                    continue    
                tmp.append(candidates[j])
                j = 0
                continue
            j += 1
        if len(tmp) > 2:
            return tmp
    return False



def candidateStraightFlushOnTable(candidates):
    length = len(candidates)
    if length < 2:
        return False
    if candidates[1][CARD_NMBR] == "1":
        return False
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

    if 15 in numbers or 0 in numbers:
        return False
    
    for i in range(0, length - 1):
        if numbers[i + 1] - numbers[i] != 1:
            return False
        if colors[i] != colors[i + 1]:
            return False
    return True



def candidateFlushOnTable(candidates):
    length = len(candidates)
    if length > 4:
        return False
    for i in range(0, length):
        if candidates[i][CARD_CLR] == "W":
            continue
        for j in range(0, length):
            if i == j:
                continue
            if candidates[j][CARD_CLR] == "W":
                continue
            if candidates[i][CARD_NMBR] != candidates[j][CARD_NMBR]:
                return False
            if candidates[i][CARD_CLR] == candidates[j][CARD_CLR]:
                return False
    return True
            



def check(comb, candidates):
    cnt = 0
    for i in comb:
        if candidateFlush(i) != False and candidateFlush(i) not in candidates:
            candidates.append(candidateFlush(i))
            cnt += 1
        if candidateStraightFlush(i) != False and candidateStraightFlush(i) not in candidates:
            candidates.append(candidateStraightFlush(i))
            cnt += 1
    return candidates, cnt