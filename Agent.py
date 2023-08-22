from Evaluation import *
from CheckCandidates import *
from DecideCard import *
from Display import *
import tkinter as tk
import pygame
import time
import random



def checkExit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
        else:
            mousePos = (-1, -1)

        if mousePos[0] >= WIDTH - 20 and mousePos[1] <= 20:
            pygame.quit()


def checkExit2():
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


class Agent:
    def __init__(self, cardsInHand):
        self.cardsInHand = cardsInHand
        self.cardsOnTable = []
        self.optimalCards = []
        self.unusedCards = []
        self.borrowedCard = 0
        self.eval = 0
        self.fEval = 0
        self.danger = 0
        self.isOpen = 0
        self.canOpen = 0


    def setOptimalCards(self, game):
        comb = combinations(self.cardsInHand, 5)
        candidates = []
        candidates, cnt = check(comb, candidates)

        for player in game.players:
            if len(player.cardsInHand) < 3:
                self.danger += 5

        if len(candidates) > 0:
            optimalSlots, stats = evaluation(candidates, self.cardsInHand)
            self.unusedCards = self.cardsInHand.copy()
            i = 0
            max = 0
            fMax = 0
            maxInd = 0
            fEval = finalEval(stats)
            while i < len(stats):
                checkExit()
                if fEval[i] > fMax:
                    fMax = fEval[i]
                    max = stats[i][1]
                    maxInd = i
                i += 1
            self.eval = max
            self.fEval = fMax
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

            if self.canOpen == 1:
                if self.eval > 50 or self.isOpen and len(self.cardsInHand) > 3 or self.borrowedCard != 0:
                    optimalCardsCnt = 0
                    for slot in self.optimalCards:
                        for card in slot:
                            checkExit()
                            optimalCardsCnt += 1
                    if len(self.cardsInHand) <= 5:
                        tmp = self.cardsInHand.copy()
                        if candidateFlush(tmp) != False:
                            canTmp = candidateFlush(tmp)
                            self.cardsOnTable.append(canTmp)
                            for card in self.cardsInHand:
                                checkExit()
                                if card in canTmp:
                                    tmp.pop(tmp.index(card))
                            self.cardsInHand = tmp.copy()
                        elif candidateStraightFlush(tmp) != False:
                            canTmp = candidateStraightFlush(tmp)
                            self.cardsOnTable.append(canTmp)
                            for card in self.cardsInHand:
                                checkExit()
                                if card in canTmp:
                                    tmp.pop(tmp.index(card))
                            self.cardsInHand = tmp.copy()
                            
                            for p in game.players:
                                p.danger += 3
                            self.danger -= 3

                            if len(self.cardsInHand) < 6:
                                for p in game.players:
                                    checkExit()
                                    p.danger += 3
                                self.danger -= 3
                    elif len(self.cardsInHand) > optimalCardsCnt:
                        if self.danger > 7 or (len(self.cardsInHand) - optimalCardsCnt == 1):
                            for combo in self.optimalCards:
                                for card in combo:
                                    checkExit()
                                    self.cardsInHand.pop(self.cardsInHand.index(card))
                                self.cardsOnTable.append(combo)
                            self.optimalCards = []
                            self.eval = 0
                            self.fEval = 0
                            self.isOpen = 1
                            self.borrowedCard = 0
                            
                            for p in game.players:
                                p.danger += 3
                            self.danger -= 3
        else:
            self.danger += 2


    def putCardsOnTable(self, game):
        if self.isOpen == 1:
            for player in game.players:
                if player.cardsOnTable != []:
                    if player.cardsOnTable[0] == []:
                        player.cardsOnTable.pop(0)
                    for slot in player.cardsOnTable:
                        checkExit()
                        tmpLo = slot.copy()
                        tmpHi = slot.copy()

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
                            checkExit()
                            if card[CARD_CLR] == "W":
                                tmp = tmpHi.copy()
                                tmp.append(card)
                                if candidateFlushOnTable(tmp) or candidateStraightFlushOnTable(tmp):
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.append(card)
                                    self.cardsInHand.pop(tmpCard)
                                    break
                                tmp = tmpLo.copy()
                                tmp.insert(0, card)
                                if candidateStraightFlushOnTable(tmp):
                                    tmpCard = self.cardsInHand.index(card)
                                    slot.insert(0, card)
                                    self.cardsInHand.pop(tmpCard)
                                    break

                        tmpCard = 0
                        for card in self.cardsInHand:
                            checkExit()
                            if card[CARD_CLR] == "W":
                                continue
                            tmp = tmpLo.copy()
                            tmp.insert(0, card)

                            if candidateStraightFlushOnTable(tmp):
                                tmpCard = self.cardsInHand.index(card)
                                slot.insert(0, card)
                                self.cardsInHand.pop(tmpCard)
                                break

                        tmpCard = 0
                        for card in self.cardsInHand:
                            checkExit()
                            if card[CARD_CLR] == "W":
                                continue
                            tmp = tmpHi.copy()
                            tmp.append(card)

                            if candidateFlushOnTable(tmp) or candidateStraightFlushOnTable(tmp):
                                tmpCard = self.cardsInHand.index(card)
                                slot.append(card)
                                self.cardsInHand.pop(tmpCard)
                                break



    def decideCardToThrowOut(self, game):
        tmp = decideCardToThrowOut(self.cardsInHand, self.optimalCards, self.unusedCards, game.deck, game.thrownCards, game)
        checkExit()
        if tmp == []:
            self.unusedCards = self.cardsInHand.copy()
            self.optimalCards = []
        return tmp