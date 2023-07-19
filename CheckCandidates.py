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



def candidateColorOrder(candidates):
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



def candidateOrder(candidates):
    candidates = sortCards(candidates)
    while len(candidates) < 5:
        candidates.append(("PLACEH", "0", "LDER"))
    for i in range(0, 5):
        if candidates[i][CARD_CLR] == "W":
            continue
        tmp = [candidates[i]]
        j = 0
        while j < 5:
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
                tmp.append(candidates[j])# Možda stavit uvjete u uvjete da bude malo preglednije.
                j = 0
                continue
            j += 1
        if len(tmp) > 2:
            return tmp
    return False



def check(comb, candidates):
    cnt = 0
    for i in comb:
        if candidateColorOrder(i) != False and candidateColorOrder(i) not in candidates:
            candidates.append(candidateColorOrder(i))
            cnt += 1
        if candidateOrder(i) != False and candidateOrder(i) not in candidates:
            candidates.append(candidateOrder(i))
            cnt += 1
    return candidates, cnt