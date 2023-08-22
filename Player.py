from Evaluation import *
from CheckCandidates import *
from DecideCard import *
from Display import *
from Agent import *
import tkinter as tk
import pygame
import time
import random

root = tk.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X_UNIT = WIDTH // 16
Y_UNIT = HEIGHT // 9
CARD_WIDTH = X_UNIT + 2
CARD_HEIGHT = int(Y_UNIT * 1.5) + 2
CARD_CLR = 0
CARD_NMBR = 1
PLAYER_INDEX_TO_START_POS = {"0": [X_UNIT * 5, HEIGHT - int(CARD_HEIGHT * 0.5)],
                             "1": [WIDTH - int(0.5 * X_UNIT), int(Y_UNIT * 6.5) - int(CARD_WIDTH * 0.5)],
                             "2": [X_UNIT * 10, 0 - int(CARD_HEIGHT * 0.5)],
                             "3": [0, int(HEIGHT // 9 * 2.5) + int(CARD_WIDTH * 0.5)]}

PLAYER_INDEX_TO_END_POS = {"0": [X_UNIT * 10, HEIGHT - int(CARD_HEIGHT * 0.5)],
                           "1": [WIDTH - int(0.5 * X_UNIT), int(Y_UNIT * 2.5) + int(CARD_WIDTH * 0.5)],
                           "2": [X_UNIT * 5, 0 - int(CARD_HEIGHT * 0.5)],
                           "3": [0, int(Y_UNIT * 6.5) - int(CARD_WIDTH * 0.5)]}

TABLE_CARDS_START_POS = {   "00" : [int(X_UNIT * 5),   HEIGHT - int(2.2 * CARD_HEIGHT)],
                            "01" : [int(X_UNIT * 6.7), HEIGHT - int(2.2 * CARD_HEIGHT)],
                            "02" : [int(X_UNIT * 8.2), HEIGHT - int(2.2 * CARD_HEIGHT)],
                            "03" : [int(X_UNIT * 10),  HEIGHT - int(2.2 * CARD_HEIGHT)],

                            "10" : [WIDTH - int(3.9 * CARD_WIDTH), int(Y_UNIT * 7)],
                            "11" : [WIDTH - int(3.9 * CARD_WIDTH), int(Y_UNIT * 5.3)],
                            "12" : [WIDTH - int(3.9 * CARD_WIDTH), int(Y_UNIT * 3.65)],
                            "13" : [WIDTH - int(3.9 * CARD_WIDTH), int(Y_UNIT * 2)],

                            "20" : [int(X_UNIT * 5),   int(0.7 * CARD_HEIGHT)],
                            "21" : [int(X_UNIT * 6.7), int(0.7 * CARD_HEIGHT)],
                            "22" : [int(X_UNIT * 8.2), int(0.7 * CARD_HEIGHT)],
                            "23" : [int(X_UNIT * 10),  int(0.7 * CARD_HEIGHT)],

                            "30" : [int(3 * CARD_WIDTH), int(Y_UNIT * 2)],
                            "31" : [int(3 * CARD_WIDTH), int(Y_UNIT * 3.65)],
                            "32" : [int(3 * CARD_WIDTH), int(Y_UNIT * 5.3)],
                            "33" : [int(3 * CARD_WIDTH), int(Y_UNIT * 7)]
}

TABLE_CARDS_END_POS = {     "00" : [int(X_UNIT * 5),   HEIGHT - int(1.4 * CARD_HEIGHT)],
                            "01" : [int(X_UNIT * 6.7), HEIGHT - int(1.4 * CARD_HEIGHT)],
                            "02" : [int(X_UNIT * 8.2), HEIGHT - int(1.4 * CARD_HEIGHT)],
                            "03" : [int(X_UNIT * 10),  HEIGHT - int(1.4 * CARD_HEIGHT)],

                            "10" : [WIDTH - int(2.25 * CARD_WIDTH), int(Y_UNIT * 7)],
                            "11" : [WIDTH - int(2.25 * CARD_WIDTH), int(Y_UNIT * 5.3)],
                            "12" : [WIDTH - int(2.25 * CARD_WIDTH), int(Y_UNIT * 3.65)],
                            "13" : [WIDTH - int(2.25 * CARD_WIDTH), int(Y_UNIT * 2)],

                            "20" : [int(X_UNIT * 5),   int(1.6 * CARD_HEIGHT)],
                            "21" : [int(X_UNIT * 6.7), int(1.6 * CARD_HEIGHT)],
                            "22" : [int(X_UNIT * 8.2), int(1.6 * CARD_HEIGHT)],
                            "23" : [int(X_UNIT * 10),  int(1.6 * CARD_HEIGHT)],

                            "30" : [int(1.5 * CARD_WIDTH), int(Y_UNIT * 2)],
                            "31" : [int(1.5 * CARD_WIDTH), int(Y_UNIT * 3.65)],
                            "32" : [int(1.5 * CARD_WIDTH), int(Y_UNIT * 5.3)],
                            "33" : [int(1.5 * CARD_WIDTH), int(Y_UNIT * 7)]
}

THROWN_CARDS_POS = (WIDTH // 2 - CARD_WIDTH, HEIGHT // 2 - int(0.65 * CARD_WIDTH))

def onThrowButton(mousePos):
    return mousePos[0] >= WIDTH - CARD_WIDTH - X_UNIT and mousePos[0] <= WIDTH and mousePos[1] >= HEIGHT - int(0.5 * Y_UNIT) and mousePos[1] <= HEIGHT

def onCancelButton(mousePos):
    return onThrowButton(mousePos)

def onPutDownButton(mousePos):
    return mousePos[0] >= WIDTH - CARD_WIDTH - X_UNIT and mousePos[0] <= WIDTH and mousePos[1] > HEIGHT - int(1 * Y_UNIT) and mousePos[1] <= HEIGHT - int(0.5 * Y_UNIT)

def onAutoSetButton(mousePos):
    return mousePos[0] >= WIDTH - CARD_WIDTH - X_UNIT and mousePos[0] <= WIDTH and mousePos[1] > HEIGHT - int(1.5 * Y_UNIT) and mousePos[1] <= HEIGHT - int(1 * Y_UNIT)



def mainMenu(screen, BLITS_DICT):
    bg = BLITS_DICT["bg"]
    button = BLITS_DICT["button"]
    screen.blit(bg, (0, 0))
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('x', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH - 20, 20)
    screen.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', 60)
    xPos = WIDTH // 2
    yPos = HEIGHT // 4
    text = font.render('PyRemi', True, (100, 100, 100))
    font = pygame.font.Font('freesansbold.ttf', 60)
    textRect = text.get_rect()
    textRect.center = (xPos, yPos + 5)
    screen.blit(text, textRect)
    text = font.render('PyRemi', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (xPos, yPos)
    screen.blit(text, textRect)
    yPos = HEIGHT // 2
    font = pygame.font.Font('freesansbold.ttf', 20)
    
    buttonCoords = []
    for i in range(1, 4):
        if i == 1:
            s = ""
        else:
            s = "s"
        screen.blit(button, (xPos - 2 * X_UNIT, yPos - int(0.5 * Y_UNIT)))
        text = font.render("Play with " + str(i) + " player" + s, True, (100, 100, 100))
        textRect = text.get_rect()
        textRect.center = (xPos, yPos + 3)
        screen.blit(text, textRect)
        text = font.render("Play with " + str(i) + " player" + s, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (xPos, yPos)
        screen.blit(text, textRect)
        buttonCoords.append([xPos - 2 * X_UNIT, yPos - int(0.5 * Y_UNIT), xPos + 2 * X_UNIT, yPos + int(0.5 * Y_UNIT)])
        yPos += HEIGHT // 8 
    pygame.display.update()    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
            else:
                mousePos = (-1, -1)

            if mousePos[0] >= WIDTH - 30 and mousePos[1] <= 30:
                pygame.quit()
                
            if mousePos != (-1, -1):
                for pos in buttonCoords:
                    if mousePos[0] >= pos[0] and mousePos[0] <= pos[2] and mousePos[1] >= pos[1] and mousePos[1] <= pos[3]:
                       return (buttonCoords.index(pos) + 2)



class Human:
    def __init__(self, cardsInHand):
        self.cardsInHand = cardsInHand
        self.cardsOnTable = []
        self.optimalCards = []
        self.unusedCards = []
        self.borrowedCard = 0
        self.danger = 0
        self.eval = 0
        self.fEval = 0
        self.isOpen = 0
        self.canOpen = 0
        
        
    def getCardPositions(self):
        length = len(self.cardsInHand)
        xStartPos = PLAYER_INDEX_TO_START_POS['0'][0]
        yStartPos = PLAYER_INDEX_TO_START_POS['0'][1]
        xEndPos = PLAYER_INDEX_TO_END_POS['0'][0]
        yEndPos = PLAYER_INDEX_TO_END_POS['0'][1]
        posX = xStartPos
        posY = yStartPos
        cardPos = []
        if length > 1:
            for i in range(0, length - 1):
                cardPos.append([posX, posY])
                if (xEndPos - xStartPos) // (length - 1) > 1 * CARD_WIDTH:
                    posX += int(1 * CARD_WIDTH)
                else:
                    posX += (xEndPos - xStartPos) // (length - 1)
                posY += (yEndPos - yStartPos) // (length - 1)
                cardPos[i].append(posX)
                cardPos[i].append(posY + CARD_HEIGHT)
        cardPos.append([posX, posY, posX + CARD_WIDTH, posY + CARD_HEIGHT])
        return cardPos.copy()
    


    def getTableCoords(self):
        tableCoords = []
        for key in TABLE_CARDS_START_POS:
            if key[0] == "0" or key[0] == "2":
                ht0 = 0
                wd0 = 0
                ht1 = CARD_HEIGHT
                wd1 = CARD_WIDTH
            elif key[0] == "1":
                ht0 = 0
                wd0 = 0
                wd1 = CARD_HEIGHT
                ht1 = CARD_WIDTH
            else:
                ht0 = -1 * CARD_HEIGHT
                wd0 = -1 * CARD_WIDTH
                wd1 = 0
                ht1 = 0

            x0 = min(TABLE_CARDS_START_POS[key][0], TABLE_CARDS_END_POS[key][0])
            y0 = min(TABLE_CARDS_START_POS[key][1], TABLE_CARDS_END_POS[key][1])
            x1 = max(TABLE_CARDS_START_POS[key][0], TABLE_CARDS_END_POS[key][0])
            y1 = max(TABLE_CARDS_START_POS[key][1], TABLE_CARDS_END_POS[key][1])
            tableCoords.append([key, x0 + wd0, y0 + ht0, x1 + wd1, y1 + ht1])
        return tableCoords



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



    def takeCard(self, game, tmpGame, screen, BLITS_DICT, ALL_CARDS_BLIT_DICT):
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
            displayBackground(screen, game, BLITS_DICT)
            displayPlayerCards(screen, len(game.players), ALL_CARDS_BLIT_DICT, game, -1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                else:
                    mousePos = (-1, -1)
                
                if mousePos[0] >= WIDTH - 30 and mousePos[1] <= 30:
                    pygame.quit()
                
                if mousePos[0] >= WIDTH - 60 and mousePos[0] < WIDTH - 30 and mousePos[1] <= 30:
                    return False

                if mousePos[0] >= THROWN_CARDS_POS[0] and mousePos[0] <= THROWN_CARDS_POS[0] + CARD_WIDTH:
                    if mousePos[1] >= THROWN_CARDS_POS[1] and mousePos[1] <= THROWN_CARDS_POS[1] + CARD_HEIGHT:
                        chosenPile = 1
                
                if mousePos[0] >= THROWN_CARDS_POS[0] + CARD_WIDTH and mousePos[0] <= THROWN_CARDS_POS[0] + 2 * CARD_WIDTH:
                    if mousePos[1] >= THROWN_CARDS_POS[1] and mousePos[1] <= THROWN_CARDS_POS[1] + CARD_HEIGHT:
                        chosenPile = 2
                
                if chosenPile == 1:
                    if game.thrownCards != []:
                        if self.isOpen == 1 and len(self.cardsInHand) > 1:
                            self.cardsInHand.append(game.thrownCards[-1])
                            game.thrownCards.pop(-1)
                            cardChosen = True
                        else:
                            chosenPile = -1
                            card = game.thrownCards[-1]
                            tmpGame.players[0].cardsInHand = self.cardsInHand.copy()
                            tmpGame.players[0].cardsInHand.append(card)
                            tmpGame.players[0].setOptimalCards(tmpGame)
                            possible = False
                            cardSum = 0
                            for slot in tmpGame.players[0].optimalCards:
                                if candidateStraightFlushOnTable:
                                    cardSum += evaluateCandidateSumStraightFlush(slot)
                                elif candidateFlushOnTable:
                                    cardSum += evaluateCandidateSumFlush(slot) 
                                for optimalCard in slot:
                                    if optimalCard == card:
                                        possible = True
                                        break
                                if possible:
                                    break

                            if possible and cardSum > 50:
                                self.cardsInHand.append(card)
                                game.thrownCards.pop(-1)
                                self.borrowedCard = card
                                cardChosen = True
                
                if chosenPile == 2:
                    if game.deck != []:
                        self.cardsInHand.append(game.deck[-1])
                        game.deck.pop(-1)
                        cardChosen = True
                        break
        return True



    def chooseCardsToPutDown(self, screen, game, BLITS_DICT, blitDict):
        done = False
        cardIndexes = []
        displayBackground(screen, game, BLITS_DICT)
        displayPlayerCards2(screen, len(game.players), blitDict, game, cardIndexes)
        displayPlayerButtons(screen, 0, BLITS_DICT)
        pygame.display.update()
        chosenCard = -1
        cardPos = self.getCardPositions()
        tableCoords = self.getTableCoords()
        formerTableCards = self.cardsOnTable.copy()
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                else:
                    mousePos = (-1, -1)

                if mousePos[0] >= WIDTH - 30 and mousePos[1] <= 30:
                    pygame.quit()

                for pos in cardPos:
                    if mousePos[0] >= pos[0] and mousePos[0] <= pos[2] and mousePos[1] >= pos[1] and mousePos[1] <= pos[3]:
                        chosenCard = cardPos.index(pos)
                        if chosenCard != -1:
                            if chosenCard in cardIndexes:
                                cardIndexes.pop(cardIndexes.index(chosenCard))
                            else:
                                cardIndexes.append(chosenCard)
                            chosenCard = -1
                        displayBackground(screen, game, BLITS_DICT)
                        displayPlayerCards2(screen, len(game.players), blitDict, game, cardIndexes)
                        displayPlayerButtons(screen, 0, BLITS_DICT)
                        pygame.display.update()

                if onAutoSetButton(mousePos):
                    self.setOptimalCards(game)
                    displayBackground(screen, game, BLITS_DICT)
                    displayPlayerCards2(screen, len(game.players), blitDict, game, cardIndexes)
                    displayPlayerButtons(screen, 1, BLITS_DICT)
                    pygame.display.update()

                if onPutDownButton(mousePos):
                    if len(cardIndexes) <= 5 or len(cardIndexes) >= 2 and len(self.cardsOnTable) < 4:
                        cards = []
                        if cardIndexes == []:
                            continue
                        for ind in cardIndexes:
                            cards.append(self.cardsInHand[ind])

                        if candidateFlushOnTable(cards) or candidateStraightFlushOnTable(cards):
                            self.cardsOnTable.append(cards)
                            for card in cards:
                                self.cardsInHand.pop(self.cardsInHand.index(card))
                            cardPos = self.getCardPositions()
                            chosenCard = -1
                            cardIndexes = []
                            displayBackground(screen, game, BLITS_DICT)
                            displayPlayerCards2(screen, len(game.players), blitDict, game, cardIndexes)
                            displayPlayerButtons(screen, 0, BLITS_DICT)
                            pygame.display.update()
                            break
                
                if onCancelButton(mousePos) or len(self.cardsOnTable) == 4:
                    done = True
                    displayBackground(screen, game, BLITS_DICT)
                    displayPlayerCards(screen, len(game.players), blitDict, game, -1)
                    displayPlayerButtons(screen, 1, BLITS_DICT)
                    pygame.display.update()
                    break

                for pos in tableCoords:
                    if mousePos[0] >= pos[1] and mousePos[0] <= pos[3] and mousePos[1] >= pos[2] and mousePos[1] <= pos[4]:
                        playerInd = int(pos[0][0])
                        slotInd = int(pos[0][1])
                        if playerInd > 0:
                            break
                        if slotInd > len(game.players[playerInd].cardsOnTable) - 1:
                            continue
                        slot = game.players[playerInd].cardsOnTable[slotInd]
                        if slot not in formerTableCards:
                            for card in slot:
                                self.cardsInHand.append(card)
                            self.cardsOnTable.pop(slotInd)
                            cardIndexes = []
                            cardPos = self.getCardPositions()
                            displayBackground(screen, game, BLITS_DICT)
                            displayPlayerCards2(screen, len(game.players), blitDict, game, cardIndexes)
                            displayPlayerButtons(screen, 1, BLITS_DICT)
                            pygame.display.update()



    def putCardsDown(self, screen, game, BLITS_DICT, blitDict):
        if len(self.cardsOnTable) > 3:
            return 0
        formerCardsInHand = self.cardsInHand.copy()
        if self.isOpen != 1:
            formerLength = len(self.cardsInHand)
            self.chooseCardsToPutDown(screen, game, BLITS_DICT, blitDict)
            cardSum = 0
            for slot in self.cardsOnTable:
                if candidateFlushOnTable(slot):
                    cardSum += evaluateCandidateSumFlush(slot)
                elif candidateStraightFlushOnTable(slot):
                    cardSum += evaluateCandidateSumStraightFlush(slot)

            if cardSum > 50:
                self.isOpen = 1
                if formerLength == 15 and len(self.cardsInHand) == 1:
                    return 1
                return 0
            else:
                self.cardsInHand = formerCardsInHand
                self.cardsOnTable = []
        else:
            self.chooseCardsToPutDown(screen, game, BLITS_DICT, blitDict)
                


    def pickCard(self, game, screen, blitDict, BLITS_DICT):
        cardPos = []
        length = len(self.cardsInHand)
        xStartPos = PLAYER_INDEX_TO_START_POS['0'][0]
        yStartPos = PLAYER_INDEX_TO_START_POS['0'][1]
        xEndPos = PLAYER_INDEX_TO_END_POS['0'][0]
        yEndPos = PLAYER_INDEX_TO_END_POS['0'][1]
        posX = xStartPos
        posY = yStartPos
        tableCoords = self.getTableCoords()
        if length > 1:
            for i in range(0, length - 1):
                cardPos.append([posX, posY])
                if (xEndPos - xStartPos) // (length - 1) > 1 * CARD_WIDTH:
                    posX += int(1 * CARD_WIDTH)
                else:
                    posX += (xEndPos - xStartPos) // (length - 1)
                posY += (yEndPos - yStartPos) // (length - 1)
                cardPos[i].append(posX)
                cardPos[i].append(posY + CARD_HEIGHT)
        cardPos.append([posX, posY, posX + CARD_WIDTH, posY + CARD_HEIGHT])
        
        cardThrown = False
        chosenCard = -1
        chosenCard2 = -1
        isHand = 0
        while cardThrown == False:
            for event in pygame.event.get():
                length = len(self.cardsInHand)
                posX = xStartPos
                posY = yStartPos
                cardPos = []
                if length > 1:
                    for i in range(0, length - 1):
                        cardPos.append([posX, posY])
                        if (xEndPos - xStartPos) // (length - 1) > 1 * CARD_WIDTH:
                            posX += int(1 * CARD_WIDTH)
                        else:
                            posX += (xEndPos - xStartPos) // (length - 1)
                        posY += (yEndPos - yStartPos) // (length - 1)
                        cardPos[i].append(posX)
                        cardPos[i].append(posY + CARD_HEIGHT)
                cardPos.append([posX, posY, posX + CARD_WIDTH, posY + CARD_HEIGHT])

                displayBackground(screen, game, BLITS_DICT)
                displayPlayerCards(screen, len(game.players), blitDict, game, chosenCard)
                displayPlayerButtons(screen, 1, BLITS_DICT)

                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                else:
                    mousePos = (-1, -1)

                if mousePos[0] >= WIDTH - 30 and mousePos[1] <= 30:
                    pygame.quit()

                if mousePos[0] >= WIDTH - 60 and mousePos[0] < WIDTH - 30 and mousePos[1] <= 30:
                    return False

                if len(self.cardsInHand) == 1:
                    displayBackground(screen, game, BLITS_DICT)
                    card = self.cardsInHand[0]
                    self.cardsInHand.pop(0)
                    displayCardThrow(screen, card, game, 0, blitDict, BLITS_DICT, 1)
                    pygame.display.update()
                    if isHand == 1:
                        return 1
                    cardThrown = True
                    break

                if onAutoSetButton(mousePos):
                    self.setOptimalCards(game)
                    displayBackground(screen, game, BLITS_DICT)
                    displayPlayerCards(screen, len(game.players), blitDict, game, chosenCard)
                    displayPlayerButtons(screen, 1, BLITS_DICT)
                    pygame.display.update()

                if onThrowButton(mousePos):
                    if chosenCard != -1:
                        if self.borrowedCard != 0:
                            if self.borrowedCard in self.cardsInHand:
                                break
                        self.borrowedCard = 0
                        displayBackground(screen, game, BLITS_DICT)
                        card = self.cardsInHand[chosenCard]
                        self.cardsInHand.pop(chosenCard)
                        displayCardThrow(screen, card, game, 0, blitDict, BLITS_DICT, 1)
                        displayPlayerButtons(screen, 1, BLITS_DICT)
                        pygame.display.update()
                        cardThrown = True
                        break         
                      
                elif onPutDownButton(mousePos) and self.canOpen == 1:
                    isHand = self.putCardsDown(screen, game, BLITS_DICT, blitDict)
                    chosenCard = -1
                    chosenCard2 = -1
                    length = len(self.cardsInHand)
                    posX = xStartPos
                    posY = yStartPos
                    cardPos = []
                    if length > 1:
                        for i in range(0, length - 1):
                            cardPos.append([posX, posY])
                            if (xEndPos - xStartPos) // (length - 1) > 1 * CARD_WIDTH:
                                posX += int(1 * CARD_WIDTH)
                            else:
                                posX += (xEndPos - xStartPos) // (length - 1)
                            posY += (yEndPos - yStartPos) // (length - 1)
                            cardPos[i].append(posX)
                            cardPos[i].append(posY + CARD_HEIGHT)
                    cardPos.append([posX, posY, posX + CARD_WIDTH, posY + CARD_HEIGHT])
                    displayBackground(screen, game, BLITS_DICT)
                    displayPlayerCards(screen, len(game.players), blitDict, game, -1)
                    displayPlayerButtons(screen, 1, BLITS_DICT)
                    break
                
                if chosenCard != -1 and len(self.cardsInHand) > 1 and self.isOpen == 1:
                    if mousePos[1] < HEIGHT - CARD_HEIGHT:
                        for pos in tableCoords:
                            if mousePos[0] >= pos[1] and mousePos[0] <= pos[3] and mousePos[1] >= pos[2] and mousePos[1] <= pos[4]:
                                if len(game.players) == 2:
                                    if pos[0][0] == "2":
                                        playerInd = 1
                                    elif pos[0][0] == "0":
                                        playerInd = 0
                                    elif pos[0][0] == "1":
                                        continue
                                    elif pos[0][0] == "3":
                                        continue
                                else:
                                    playerInd = int(pos[0][0])
                                slotInd = int(pos[0][1])
                                if playerInd > len(game.players) - 1:
                                    continue
                                if slotInd > len(game.players[playerInd].cardsOnTable) - 1:
                                    continue
                                slot = game.players[playerInd].cardsOnTable[slotInd]
                                
                                done = False
                                tmpLo = slot.copy()
                                tmpHi = slot.copy()
                                tmpLo.insert(0, self.cardsInHand[chosenCard])
                                tmpHi.append(self.cardsInHand[chosenCard])
                                
                                if ("W", "W", "1") in slot or ("W", "W", "2") in slot or ("W", "W", "3") in slot or ("W", "W", "4") in slot:
                                    indexes = []
                                    for card in slot:
                                        if card[CARD_CLR] == "W":
                                            indexes.append(slot.index(card))
                                    
                                    for ind in indexes:
                                        if ind == 0:
                                            if compareCards(self.cardsInHand[chosenCard], slot[1], 1) == 2 and compareCards(self.cardsInHand[chosenCard], slot[2], 1) == 1:
                                                slot[ind], self.cardsInHand[chosenCard] = self.cardsInHand[chosenCard], slot[ind]
                                                chosenCard = -1
                                                break
                                            if compareCards(self.cardsInHand[chosenCard], slot[1], 1) == 2 and compareCards(self.cardsInHand[chosenCard], slot[2], 1) == 2 and len(slot) == 4:
                                                slot[ind], self.cardsInHand[chosenCard] = self.cardsInHand[chosenCard], slot[ind]
                                                chosenCard = -1
                                                break
                                        elif ind == len(slot) - 1:
                                            if compareCards(self.cardsInHand[chosenCard], slot[-2], 1) == 2 and compareCards(self.cardsInHand[chosenCard], slot[-3], 1) == 1:
                                                slot[ind], self.cardsInHand[chosenCard] = self.cardsInHand[chosenCard], slot[ind]
                                                chosenCard = -1
                                                break
                                            if compareCards(self.cardsInHand[chosenCard], slot[-2], 1) == 2 and compareCards(self.cardsInHand[chosenCard], slot[-3], 1) == 2 and len(slot) == 4:
                                                slot[ind], self.cardsInHand[chosenCard] = self.cardsInHand[chosenCard], slot[ind]
                                                chosenCard = -1
                                                break
                                        else:
                                            if compareCards(self.cardsInHand[chosenCard], slot[ind - 1], 1) == 2 and compareCards(self.cardsInHand[chosenCard], slot[ind + 1], 1) == 2:
                                                if slot[ind - 1][CARD_CLR] != slot[ind + 1] and len == 4:
                                                    slot[ind], self.cardsInHand[chosenCard] = self.cardsInHand[chosenCard], slot[ind]
                                                    chosenCard = -1
                                                    break
                                                else:
                                                    slot[ind], self.cardsInHand[chosenCard] = self.cardsInHand[chosenCard], slot[ind]
                                                    chosenCard = -1
                                                    break

                                
                                tmpCard = 0
                                if self.cardsInHand[chosenCard][CARD_CLR] == "W":
                                    if candidateFlushOnTable(tmpHi) or candidateStraightFlushOnTable(tmpHi):
                                        tmpCard = chosenCard
                                        slot.append(self.cardsInHand[chosenCard])
                                        self.cardsInHand.pop(chosenCard)
                                        chosenCard = -1
                                    if candidateStraightFlushOnTable(tmpLo):
                                        tmpCard = chosenCard
                                        slot.insert(0, self.cardsInHand[chosenCard])
                                        self.cardsInHand.pop(chosenCard)
                                        chosenCard = -1
                                else:
                                    tmpCard = 0

                                    if candidateStraightFlushOnTable(tmpLo):
                                        tmpCard = chosenCard
                                        slot.insert(0, self.cardsInHand[chosenCard])
                                        self.cardsInHand.pop(tmpCard)
                                        chosenCard = -1
                                    
                                    tmpCard = 0

                                    if candidateFlushOnTable(tmpHi) or candidateStraightFlushOnTable(tmpHi):
                                        tmpCard = chosenCard
                                        slot.append(self.cardsInHand[chosenCard])
                                        self.cardsInHand.pop(tmpCard)
                                        chosenCard = -1

                for pos in cardPos:
                    if len(mousePos) < 2:
                        break
                    if mousePos[1] < HEIGHT - CARD_HEIGHT:
                        break
                    if mousePos[0] >= pos[0] and mousePos[0] <= pos[2] and mousePos[1] >= pos[1] and mousePos[1] <= pos[3]:
                        if chosenCard != -1:
                            chosenCard2 = cardPos.index(pos)
                            if chosenCard == chosenCard2:
                                chosenCard = -1
                                chosenCard2 = -1
                                displayBackground(screen, game, BLITS_DICT)
                                displayPlayerCards(screen, len(game.players), blitDict, game, -1)
                                displayPlayerButtons(screen, 1, BLITS_DICT)
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
                        displayBackground(screen, game, BLITS_DICT)
                        displayPlayerCards(screen, len(game.players), blitDict, game, chosenCard)
                        displayPlayerButtons(screen, 1, BLITS_DICT)
                        pygame.display.update()
