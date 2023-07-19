from Evaluation import *
from CheckCandidates import *
from DecideCard import *
from Display import *
import tkinter as tk
import pygame
import time
import random

root = tk.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight() - 60
CARD_WIDTH = WIDTH // 16
CARD_HEIGHT = int(HEIGHT // 9 * 1.5)
CARD_CLR = 0
CARD_NMBR = 1
PLAYER_INDEX_TO_START_POS = {"0": [WIDTH // 2, HEIGHT - CARD_HEIGHT],
                             "1": [WIDTH - CARD_WIDTH, int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5)],
                             "2": [WIDTH // 2 + WIDTH // 4 - CARD_WIDTH, 0],
                             "3": [WIDTH // 4 + int(0.75 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5)]}

PLAYER_INDEX_TO_END_POS = {"0": [WIDTH // 2 + WIDTH // 4 - CARD_WIDTH, HEIGHT - CARD_HEIGHT],
                           "1": [WIDTH - CARD_WIDTH, int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5)],
                           "2": [WIDTH // 2, 0],
                           "3": [WIDTH // 4 + int(0.75 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5)]}

TABLE_CARDS_START_POS = {   "00" : [WIDTH // 2, HEIGHT - int(2.5 * CARD_HEIGHT)],
                            "01" : [WIDTH // 2 + CARD_WIDTH, HEIGHT - int(2.5 * CARD_HEIGHT)],
                            "02" : [WIDTH // 2 + 2 * CARD_WIDTH, HEIGHT - int(2.5 * CARD_HEIGHT)],
                            "03" : [WIDTH // 2 + 3 * CARD_WIDTH, HEIGHT - int(2.5 * CARD_HEIGHT)],
                            "10" : [WIDTH - int(3 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5)],
                            "11" : [WIDTH - int(3 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5) - CARD_WIDTH],
                            "12" : [WIDTH - int(3 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5) - 2 * CARD_WIDTH],
                            "13" : [WIDTH - int(3 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5) - 3 * CARD_WIDTH],
                            "20" : [WIDTH // 2, int(1 * CARD_HEIGHT)],
                            "21" : [WIDTH // 2 + CARD_WIDTH, int(1 * CARD_HEIGHT)],
                            "22" : [WIDTH // 2 + 2 * CARD_WIDTH, int(1 * CARD_HEIGHT)],
                            "23" : [WIDTH // 2 + 3 * CARD_WIDTH, int(1 * CARD_HEIGHT)],
                            "30" : [WIDTH // 4 + int(2.9 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5)],
                            "31" : [WIDTH // 4 + int(2.9 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5) + CARD_WIDTH],
                            "32" : [WIDTH // 4 + int(2.9 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5) + 2 * CARD_WIDTH],
                            "33" : [WIDTH // 4 + int(2.9 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5) + 3 * CARD_WIDTH]
}

TABLE_CARDS_END_POS = {     "00" : [WIDTH // 2, HEIGHT - int(2 * CARD_HEIGHT)],
                            "01" : [WIDTH // 2 + CARD_WIDTH, HEIGHT - int(2 * CARD_HEIGHT)],
                            "02" : [WIDTH // 2 + 2 * CARD_WIDTH, HEIGHT - int(2 * CARD_HEIGHT)],
                            "03" : [WIDTH // 2 + 3 * CARD_WIDTH, HEIGHT - int(2 * CARD_HEIGHT)],
                            "10" : [WIDTH - int(2.25 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5)],
                            "11" : [WIDTH - int(2.25 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5) + CARD_WIDTH],
                            "12" : [WIDTH - int(2.25 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5) + 2 * CARD_WIDTH],
                            "13" : [WIDTH - int(2.25 * CARD_WIDTH), int(HEIGHT // 9 * 6.5) - int(CARD_WIDTH * 0.5) + 3 * CARD_WIDTH],
                            "20" : [WIDTH // 2, int(1.7 * CARD_HEIGHT)],
                            "21" : [WIDTH // 2 + CARD_WIDTH, int(1.7 * CARD_HEIGHT)],
                            "22" : [WIDTH // 2 + 2 * CARD_WIDTH, int(1.7 * CARD_HEIGHT)],
                            "23" : [WIDTH // 2 + 3 * CARD_WIDTH, int(1.7 * CARD_HEIGHT)],
                            "30" : [WIDTH // 4 + int(2 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5)],
                            "31" : [WIDTH // 4 + int(2 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5) + CARD_WIDTH],
                            "32" : [WIDTH // 4 + int(2 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5) + 2 * CARD_WIDTH],
                            "33" : [WIDTH // 4 + int(2 * CARD_WIDTH), int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5) + 3 * CARD_WIDTH]
}

THROWN_CARDS_POS = (WIDTH // 2 + CARD_WIDTH, HEIGHT // 2 - int(0.65 * CARD_WIDTH))


def onButton1(mousePos):
    return mousePos[0] >= WIDTH - 2 * CARD_WIDTH and mousePos[0] <= WIDTH and mousePos[1] >= HEIGHT - int(0.75 * CARD_HEIGHT) and mousePos[1] <= HEIGHT

def onButton2(mousePos):
    return mousePos[0] >= WIDTH - 2 * CARD_WIDTH and mousePos[0] <= WIDTH and mousePos[1] >= HEIGHT - int(1.25 * CARD_HEIGHT) and mousePos[1] <= HEIGHT - int(0.75 * CARD_HEIGHT)


class Human:
    def __init__(self, cardsInHand):
        self.cardsInHand = cardsInHand
        self.cardsOnTable = []
        self.optimalCards = []
        self.unusedCards = []
        self.borrowedCard = 0
        self.danger = 0
        self.eval = 0
        self.isOpen = 0

    def setOptimalCards(self, game):
        comb = combinations(self.cardsInHand, 5)
        candidates = []
        candidates, cnt = check(comb, candidates)

        if cnt > 0:
            optimalSlots, stats = evaluation(candidates, self.cardsInHand)
            self.unusedCards = self.cardsInHand.copy()
            i = 0
            max = 0
            maxInd = 0
            while i < len(stats):
                if stats[i][1] > max:
                    max = stats[i][1]
                    maxInd = i
                i += 1
            self.eval = max
            for can in optimalSlots[maxInd]:
                self.unusedCards = updateAvailableCards(can, self.unusedCards)
            self.optimalCards = optimalSlots[maxInd]

            tmp = []
            for combos in self.optimalCards:
                for card in combos:
                    tmp.append(card)
            
            for card in self.unusedCards:
                tmp.append(card)

            self.cardsInHand = tmp.copy()

    def decideCardToThrowOut(self, game):
        pass

    def putCardOnTable(self, game):
        pass

    def takeCard(self, game):
        if game.deck == []:
            cards = game.thrownCards.copy()
            game.thrownCards = []
            game.deck = []
            while len(cards) != len(game.deck):
                tmp = random.choice(cards)
                if tmp not in game.deck:
                    game.deck.append(tmp)

        if len(self.cardsInHand) == 15:
            return

        chosenPile = -1
        cardChosen = False
        while cardChosen == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                else:
                    mousePos = (-1, -1)
                
                if mousePos[0] >= THROWN_CARDS_POS[0] and mousePos[0] <= THROWN_CARDS_POS[0] + CARD_WIDTH:
                    if mousePos[1] >= THROWN_CARDS_POS[1] and mousePos[1] <= THROWN_CARDS_POS[1] + CARD_HEIGHT:
                        chosenPile = 1
                
                if mousePos[0] >= THROWN_CARDS_POS[0] + CARD_WIDTH and mousePos[0] <= THROWN_CARDS_POS[0] + 2 * CARD_WIDTH:
                    if mousePos[1] >= THROWN_CARDS_POS[1] and mousePos[1] <= THROWN_CARDS_POS[1] + CARD_HEIGHT:
                        chosenPile = 2
                
                if chosenPile == 1:
                    if game.thrownCards != []:
                        if self.isOpen:
                            self.cardsInHand.append(game.thrownCards[-1])
                            self.borrowedCard = game.thrownCards[-1]
                            game.thrownCards.pop(-1)
                            cardChosen = True
                        #else:
                        #    card = game.thrownCards[-1]
                        #    tmpPlayer = Human(self.cardsInHand.copy())
                        #    tmpPlayer.cardsInHand.append(card)
                        #    tmpPlayer.setOptimalCards(game)
                        #    if card in tmpPlayer.optimalCards:
                        #        
                        #        self.cardsInHand.append(card)
                        #        game.thrownCards.pop(-1)
                        #        cardChosen = True
                
                if chosenPile == 2:
                    if game.deck != []:
                        self.cardsInHand.append(game.deck[-1])
                        game.deck.pop(-1)
                        cardChosen = True


    def chooseCardsToPutDown(self, screen, game, bg, back, blitDict, cardPos):
        done = False
        cardIndexes = []
        displayBackground(screen, game, bg, back)
        displayPlayerCards2(screen, len(game.players), blitDict, game, cardIndexes)
        displayPlayerButtons(screen, 0)
        pygame.display.update()
        chosenCard = -1
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                else:
                    mousePos = (-1, -1)

                for pos in cardPos:
                    if mousePos[0] >= pos[0] and mousePos[0] <= pos[2] and mousePos[1] >= pos[1] and mousePos[1] <= pos[3]:
                        chosenCard = cardPos.index(pos)
                        if chosenCard != -1:
                            if chosenCard in cardIndexes:
                                cardIndexes.pop(cardIndexes.index(chosenCard))
                            else:
                                cardIndexes.append(chosenCard)
                            chosenCard = -1
                        displayBackground(screen, game, bg, back)
                        displayPlayerCards2(screen, len(game.players), blitDict, game, cardIndexes)
                        displayPlayerButtons(screen, 0)
                        pygame.display.update()

                if onButton1(mousePos):
                    done = True
                    displayBackground(screen, game, bg, back)
                    displayPlayerCards(screen, len(game.players), blitDict, game, -1)
                    displayPlayerButtons(screen, 1)
                    pygame.display.update()
                    break

                if onButton2(mousePos):
                    if len(cardIndexes) > 2:
                        if len(cardIndexes) < 6 and self.isOpen == 1:
                            lst = []
                            for i in cardIndexes:
                                lst.append(self.cardsInHand[i])
                            tmp = lst.copy()
                            if candidateColorOrder(tmp) != False:
                                tmp2 = self.cardsInHand.copy()
                                canTmp = candidateColorOrder(tmp)
                                self.cardsOnTable.append(canTmp)
                                for card in self.cardsInHand:
                                    if card in canTmp:
                                        tmp2.pop(tmp2.index(card))
                                self.cardsInHand = tmp2.copy()
                                print(self.eval)
                                done = True
                                self.eval = 0
                                for p in game.players:
                                    p.danger += 2
                                self.danger -= 2
                                break
                            elif candidateOrder(tmp) != False:
                                tmp2 = self.cardsInHand.copy()
                                canTmp = candidateOrder(tmp)
                                self.cardsOnTable.append(canTmp)
                                for card in self.cardsInHand:
                                    if card in canTmp:
                                        tmp2.pop(tmp2.index(card))
                                self.cardsInHand = tmp2.copy()
                                print(self.eval)
                                done = True
                                self.eval = 0
                                for p in game.players:
                                    p.danger += 2
                                self.danger -= 2
                                break
                        else:
                            chosenCard = -1
                            cardsToCheck = []
                            for ind in cardIndexes:
                                cardsToCheck.append(self.cardsInHand[ind])
                            
                            cardsToCheck = sortCards(cardsToCheck).copy()
                            comb = combinations(cardsToCheck, 5)
                            candidates = []
                            candidates, cnt = check(comb, candidates)

                            if cnt > 0:
                                optimalSlots, stats = evaluation(candidates, self.cardsInHand)
                                i = 0
                                max = 0
                                maxInd = 0
                                
                                while i < len(stats):
                                    if stats[i][1] > max:
                                        max = stats[i][1]
                                        maxInd = i
                                    i += 1
                                self.eval = max

                                optimalCards = optimalSlots[maxInd]
                                print(self.eval)

                                tmp = []
                                cnt = 0
                                for combo in optimalCards:
                                    for card in combo:
                                        tmp.append(card)

                                if len(cardsToCheck) == len(tmp):
                                    if self.eval > 50 or self.isOpen == 1 and len(tmp) < len(self.cardsInHand):
                                        if self.borrowedCard == 0:
                                            for combo in optimalCards:
                                                self.cardsOnTable.append(combo)
                                            for card in tmp:
                                                self.cardsInHand.pop(self.cardsInHand.index(card))
                                            self.eval = 0
                                            self.isOpen = 1
                                            done = True
                                            self.eval = 0
                                            break
                                        else:
                                            if self.borrowedCard in optimalCards:
                                                for combo in optimalCards:
                                                    self.cardsOnTable.append(combo)
                                                for card in tmp:
                                                    self.cardsInHand.pop(self.cardsInHand.index(card))
                                                self.eval = 0
                                                self.isOpen = 1
                                                done = True
                                                self.eval = 0
                                                self.borrowedCard = 0
                                                break
                                    
                        displayBackground(screen, game, bg, back)
                        displayPlayerCards2(screen, len(game.players), blitDict, game, cardIndexes)
                        displayPlayerButtons(screen, 0)
                        pygame.display.update()


    def pickCard(self, game, screen, blitDict, bg, back):
        cardPos = []
        length = len(self.cardsInHand)
        xStartPos = PLAYER_INDEX_TO_START_POS['0'][0]
        yStartPos = PLAYER_INDEX_TO_START_POS['0'][1]
        xEndPos = PLAYER_INDEX_TO_END_POS['0'][0]
        yEndPos = PLAYER_INDEX_TO_END_POS['0'][1]
        posX = xStartPos
        posY = yStartPos
        tableCoords = []
        for key in TABLE_CARDS_START_POS:
            if key[0] == "0" or key[0] == "2":
                ht = CARD_HEIGHT
                wd = CARD_WIDTH
            if key[0] == "1" or key[0] == "3":
                wd = CARD_HEIGHT
                ht = CARD_WIDTH
            tableCoords.append([key, TABLE_CARDS_START_POS[key][0], TABLE_CARDS_START_POS[key][1], TABLE_CARDS_END_POS[key][0] + wd, TABLE_CARDS_END_POS[key][1] + ht])

        print(tableCoords)
        if length > 1:
            for i in range(0, length - 1):
                cardPos.append([posX, posY])
                if (xEndPos - xStartPos) // (length - 1) > 0.5 * CARD_WIDTH:
                    posX += int(0.5 * CARD_WIDTH)
                else:
                    posX += (xEndPos - xStartPos) // (length - 1)
                posY += (yEndPos - yStartPos) // (length - 1)
                cardPos[i].append(posX)
                cardPos[i].append(posY + CARD_HEIGHT)
        cardPos.append([posX, posY, posX + CARD_WIDTH, posY + CARD_HEIGHT])
        
        cardThrown = False
        chosenCard = -1
        chosenCard2 = -1
        while cardThrown == False:
            for event in pygame.event.get():
                length = len(self.cardsInHand)
                posX = xStartPos
                posY = yStartPos
                cardPos = []
                if length > 1:
                    for i in range(0, length - 1):
                        cardPos.append([posX, posY])
                        if (xEndPos - xStartPos) // (length - 1) > 0.5 * CARD_WIDTH:
                            posX += int(0.5 * CARD_WIDTH)
                        else:
                            posX += (xEndPos - xStartPos) // (length - 1)
                        posY += (yEndPos - yStartPos) // (length - 1)
                        cardPos[i].append(posX)
                        cardPos[i].append(posY + CARD_HEIGHT)
                cardPos.append([posX, posY, posX + CARD_WIDTH, posY + CARD_HEIGHT])

                displayBackground(screen, game, bg, back)
                displayPlayerCards(screen, len(game.players), blitDict, game, chosenCard)
                displayPlayerButtons(screen, 1)

                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                else:
                    mousePos = (-1, -1)

                if onButton1(mousePos):
                    if chosenCard != -1 and self.eval < 50:
                        displayBackground(screen, game, bg, back)
                        card = self.cardsInHand[chosenCard]
                        self.cardsInHand.pop(chosenCard)
                        displayCardThrow(screen, card, game, 0, blitDict, bg, back, 1)
                        displayPlayerButtons(screen, 1)
                        pygame.display.update()
                        cardThrown = True                
                elif onButton2(mousePos):
                    self.chooseCardsToPutDown(screen, game, bg, back, blitDict, cardPos)
                    chosenCard = -1
                    chosenCard2 = -1
                    length = len(self.cardsInHand)
                    posX = xStartPos
                    posY = yStartPos
                    cardPos = []
                    if length > 1:
                        for i in range(0, length - 1):
                            cardPos.append([posX, posY])
                            if (xEndPos - xStartPos) // (length - 1) > 0.5 * CARD_WIDTH:
                                posX += int(0.5 * CARD_WIDTH)
                            else:
                                posX += (xEndPos - xStartPos) // (length - 1)
                            posY += (yEndPos - yStartPos) // (length - 1)
                            cardPos[i].append(posX)
                            cardPos[i].append(posY + CARD_HEIGHT)
                    cardPos.append([posX, posY, posX + CARD_WIDTH, posY + CARD_HEIGHT])
                    displayBackground(screen, game, bg, back)
                    displayPlayerCards(screen, len(game.players), blitDict, game, -1)
                    displayPlayerButtons(screen, 1)
                    break

                
                if chosenCard != -1:# and self.isOpen == 1:
                    if mousePos[1] < HEIGHT - CARD_HEIGHT:
                        for pos in tableCoords:
                            if mousePos[0] >= pos[1] and mousePos[0] <= pos[3] and mousePos[1] >= pos[2] and mousePos[1] <= pos[4]:
                                playerInd = int(pos[0][0])
                                slotInd = int(pos[0][1])
                                print(str(playerInd) + " " + str(slotInd))
                                if slotInd > len(game.players[playerInd].cardsOnTable) - 1:
                                    continue
                                if playerInd > len(game.players) - 1:
                                    continue
                                slot = game.players[playerInd].cardsOnTable[slotInd]

                                if len(slot) > 0:
                                    if self.cardsInHand[chosenCard][CARD_CLR] == "W":
                                        if compareCards(slot[-1], slot[-3], 1) == 1:
                                            if slot[-1][CARD_NMBR] != "1":
                                                game.players[playerInd].cardsOnTable[slotInd].append(self.cardsInHand[chosenCard])
                                                self.cardsInHand.pop(chosenCard)
                                            elif slot[0][CARD_NMBR] != "1":
                                                game.players[playerInd].cardsOnTable[slotInd].insert(0, self.cardsInHand[chosenCard])
                                                self.cardsInHand.pop(chosenCard)
                                        if slot[-1][CARD_NMBR] == slot[-2][CARD_NMBR] or slot[-1][CARD_NMBR] == slot[-3][CARD_NMBR] or slot[-2][CARD_NMBR] == slot[-3][CARD_NMBR]:
                                                game.players[playerInd].cardsOnTable[slotInd].append(self.cardsInHand[chosenCard])
                                                self.cardsInHand.pop(chosenCard)
                                    else:
                                        if compareCards(slot[-1], self.cardsInHand[chosenCard], 1) == 2 and compareCards(slot[-2], self.cardsInHand[chosenCard], 1) == 1:
                                            game.players[playerInd].cardsOnTable[slotInd].append(self.cardsInHand[chosenCard])
                                            self.cardsInHand.pop(chosenCard)
                                        if compareCards(slot[0], self.cardsInHand[chosenCard], 1) == 2 and compareCards(slot[1], self.cardsInHand[chosenCard], 1) == 1:
                                            game.players[playerInd].cardsOnTable[slotInd].insert(0, self.cardsInHand[chosenCard])
                                            self.cardsInHand.pop(chosenCard)
                                    break
                

                                            

                for pos in cardPos:
                    if len(mousePos) < 2:
                        break
                    if mousePos[0] >= pos[0] and mousePos[0] <= pos[2] and mousePos[1] >= pos[1] and mousePos[1] <= pos[3]:
                        if chosenCard != -1:
                            chosenCard2 = cardPos.index(pos)
                            if chosenCard == chosenCard2:
                                chosenCard = -1
                                chosenCard2 = -1
                                displayBackground(screen, game, bg, back)
                                displayPlayerCards(screen, len(game.players), blitDict, game, -1)
                                displayPlayerButtons(screen, 1)
                                pygame.display.update()
                                continue
                            if chosenCard - chosenCard2 == 1 or chosenCard2 - chosenCard == 1:
                                self.cardsInHand[chosenCard], self.cardsInHand[chosenCard2] = self.cardsInHand[chosenCard2], self.cardsInHand[chosenCard]
                            else:
                                self.cardsInHand.insert(chosenCard2 + 1, self.cardsInHand[chosenCard])
                                if chosenCard < chosenCard2:
                                    self.cardsInHand.pop(chosenCard)
                                if chosenCard > chosenCard2:
                                    self.cardsInHand.pop(chosenCard + 1)
                                    
                            chosenCard = -1
                            chosenCard2 = -1
                        else:
                            chosenCard = cardPos.index(pos)
                        displayBackground(screen, game, bg, back)
                        displayPlayerCards(screen, len(game.players), blitDict, game, chosenCard)
                        displayPlayerButtons(screen, 1)
                        pygame.display.update()

# -------------------------------------------------------------------------------------------------------------------------------------

class Agent:
    def __init__(self, cardsInHand):
        self.cardsInHand = cardsInHand
        self.cardsOnTable = []
        self.optimalCards = []
        self.unusedCards = []
        self.eval = 0
        self.danger = 0
        self.isOpen = 0


    def setOptimalCards(self, game):
        comb = combinations(self.cardsInHand, 5)
        candidates = []
        candidates, cnt = check(comb, candidates)

        if len(candidates) > 0:
            optimalSlots, stats = evaluation(candidates, self.cardsInHand)
            self.unusedCards = self.cardsInHand.copy()
            i = 0
            max = 0
            maxInd = 0
            while i < len(stats):
                if stats[i][1] > max:
                    max = stats[i][1]
                    maxInd = i
                i += 1
            self.eval = max
            for can in optimalSlots[maxInd]:
                self.unusedCards = updateAvailableCards(can, self.unusedCards)
            self.optimalCards = optimalSlots[maxInd]

            tmp = []
            for combos in self.optimalCards:
                for card in combos:
                    tmp.append(card)
            
            for card in self.unusedCards:
                tmp.append(card)

            self.cardsInHand = tmp.copy()

            if self.eval > 50 or self.isOpen and len(self.cardsInHand) > 3:
                if len(self.cardsInHand) <= 5:
                    tmp = self.cardsInHand.copy()
                    if candidateColorOrder(tmp) != False:
                        canTmp = candidateColorOrder(tmp)
                        self.cardsOnTable.append(canTmp)
                        for card in self.cardsInHand:
                            if card in canTmp:
                                tmp.pop(tmp.index(card))
                        self.cardsInHand = tmp.copy()
                    elif candidateOrder(tmp) != False:
                        canTmp = candidateOrder(tmp)
                        self.cardsOnTable.append(canTmp)
                        for card in self.cardsInHand:
                            if card in canTmp:
                                tmp.pop(tmp.index(card))
                        self.cardsInHand = tmp.copy()
                        
                        for p in game.players:
                            p.danger += 2
                        self.danger -= 2

                        if len(self.cardsInHand) < 6:
                            for p in game.players:
                                p.danger += 2
                            self.danger -= 2
                elif len(self.cardsInHand) > len(self.optimalCards):
                    if self.danger > 0 or (self.danger < 0 and len(self.cardsInHand) - len(self.optimalCards) == 1):
                        for combo in self.optimalCards:
                            for card in combo:
                                self.cardsInHand.pop(self.cardsInHand.index(card))
                            self.cardsOnTable.append(combo)
                        self.optimalCards = []
                        self.eval = 0
                        self.isOpen = 1
                        
                        for p in game.players:
                            p.danger += 2
                        self.danger -= 2


    def putCardsOnTable(self, game):
        if self.isOpen == 1:
            for player in game.players:
                if player.cardsOnTable != []:
                    if player.cardsOnTable[0] == []:
                        player.cardsOnTable.pop(0)
                    for slot in player.cardsOnTable:
                        done = False
                        tmpLo = slot.copy()
                        tmpHi = slot.copy()
                        while len(tmpHi) > 4:
                            tmpHi.pop(0)
                        while len(tmpLo) > 4:
                            tmpLo.pop(-1)

                        if ("W", "W", "1") in slot or ("W", "W", "2") in slot or ("W", "W", "3") in slot or ("W", "W", "4") in slot:
                            ind = -1
                            for card in slot:
                                if card[CARD_CLR] == "W":
                                    ind = slot.index(card)
                            for card in self.cardsInHand:
                                if ind == 0:
                                    if compareCards(card, slot[1], 1) == 2 and compareCards(card, slot[2], 1) == 1:
                                        slot[ind], self.cardsInHand[self.cardsInHand.index(card)] = self.cardsInHand[self.cardsInHand.index(card)], slot[ind]
                                    if compareCards(card, slot[1], 1) == 2 and compareCards(card, slot[2], 1) == 2 and len(slot) == 4:
                                        slot[ind], self.cardsInHand[self.cardsInHand.index(card)] = self.cardsInHand[self.cardsInHand.index(card)], slot[ind]
                                elif ind == len(slot) - 1:
                                    if compareCards(card, slot[-2], 1) == 2 and compareCards(card, slot[-3], 1) == 1:
                                        slot[ind], self.cardsInHand[self.cardsInHand.index(card)] = self.cardsInHand[self.cardsInHand.index(card)], slot[ind]
                                    if compareCards(card, slot[-2], 1) == 2 and compareCards(card, slot[-3], 1) == 2 and len(slot) == 4:
                                        slot[ind], self.cardsInHand[self.cardsInHand.index(card)] = self.cardsInHand[self.cardsInHand.index(card)], slot[ind]
                                else:
                                    if compareCards(card, slot[ind - 1], 1) == 2 and compareCards(card, slot[ind + 1], 1) == 2:
                                        if slot[ind - 1][CARD_CLR] != slot[ind + 1] and len == 4:
                                            slot[ind], self.cardsInHand[self.cardsInHand.index(card)] = self.cardsInHand[self.cardsInHand.index(card)], slot[ind]
                                        else:
                                            slot[ind], self.cardsInHand[self.cardsInHand.index(card)] = self.cardsInHand[self.cardsInHand.index(card)], slot[ind]


                        tmpCard = 0
                        for card in self.cardsInHand:
                            if card[CARD_CLR] == "W":
                                if slot[0][CARD_NMBR] == slot[1][CARD_NMBR] or slot[0][CARD_NMBR] == slot[2][CARD_NMBR] or slot[1][CARD_NMBR] == slot[2][CARD_NMBR] and len(slot) < 4:
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.append(card)
                                    done = True
                                    break
                                if compareCards(card, slot[-1], 1) == 2 and compareCards(card, slot[-2], 1) == 2 and slot[-1][CARD_NMBR] != "1":
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.append(card)
                                    done = True
                                    break
                                if compareCards(card, slot[0], 1) == 2 and compareCards(card, slot[1], 1) == 2 and slot[0][CARD_NMBR] != "1":
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.insert(0, card)
                                    done = True
                                    break
                                
                        if done:
                            self.cardsInHand.pop(tmpCard)
                            done = False

                        tmpCard = 0
                        for card in self.cardsInHand:
                            tmp = tmpLo.copy()
                            tmp.insert(0, card)

                            if candidateColorOrder(tmp) != False:
                                canTmp = candidateColorOrder(tmp)
                                if len(canTmp) == len(tmpLo) + 1 and canTmp[0] == card and compareCards(canTmp[0], canTmp[1], 1) == 2:
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.insert(0, card)
                                    done = True
                                    break
                            elif candidateOrder(tmp) != False:
                                canTmp = candidateOrder(tmp)
                                if len(canTmp) == len(tmpLo) + 1 and canTmp[0] == card and compareCards(canTmp[0], canTmp[1], 1) == 2:
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.insert(0, card)
                                    done = True
                                    break
                                
                        if done:
                            self.cardsInHand.pop(tmpCard)
                            done = False

                        tmpCard = 0
                        for card in self.cardsInHand:
                            tmp = tmpHi.copy()
                            tmp.append(card)

                            if candidateColorOrder(tmp) != False:
                                canTmp = candidateColorOrder(tmp)
                                if len(canTmp) == len(tmpHi) + 1 and canTmp[-1] == card and compareCards(canTmp[0], canTmp[1], 1) == 2:
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.append(card)
                                    done = True
                                    break
                            elif candidateOrder(tmp) != False:
                                canTmp = candidateOrder(tmp)
                                if len(canTmp) == len(tmpHi) + 1 and canTmp[-1] == card and compareCards(canTmp[0], canTmp[1], 1) == 2:
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.append(card)
                                    done = True
                                    break
                                
                        if done:
                            self.cardsInHand.pop(tmpCard)


    def decideCardToThrowOut(self, game):
        tmp = decideCardToThrowOut(self.cardsInHand, self.optimalCards, self.unusedCards, game.deck, game.thrownCards, game)
        if tmp == []:
            self.unusedCards = self.cardsInHand.copy()
            self.optimalCards = []
        return tmp