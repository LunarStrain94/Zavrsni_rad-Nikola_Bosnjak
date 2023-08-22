import random
from CheckCandidates import *
from Player import *
from Agent import *

class Game:
    def __init__(self, playerCount):
        self.playerCount = playerCount
        self.leaderboard = []
        self.players = []
        self.round = 1
        for i in range(0, playerCount):
            if i == 0:
                self.players.append(Human([]))
            else:
                self.players.append(Agent([]))
        colors = ["♠", "♥", "♣", "♦"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        self.deck = []
        for c in colors:
            for n in numbers:
                self.cards.append((c, n, "1"))
                self.cards.append((c, n, "2"))
        for i in range(0, 4):
            self.cards.append(("W", "W", str(i + 1)))
        self.thrownCards = []

    def shuffle(self, dealer):
        cards = self.cards.copy()
        self.thrownCards = []
        self.deck = []
        while len(cards) != len(self.deck):
            tmp = random.choice(cards)
            if tmp not in self.deck:
                self.deck.append(tmp)
        
        for i in range(0, self.playerCount):
            self.players[i].cardsInHand = []
            self.players[i].cardsOnTable = []
            self.players[i].optimalCards = []
            self.players[i].unusedCards = []
            self.players[i].borrowedCard = 0
            self.players[i].danger = 0
            self.players[i].isOpen = 0
            self.players[i].canOpen = 0

        for i in range(0, 7):
            for j in range(dealer - self.playerCount + 1, dealer + 1):
                if i == 0 and dealer - self.playerCount + 1 == j:
                    for k in range(0, 3):
                        self.players[j].cardsInHand.append(self.deck[0])
                        self.deck.pop(0)
                else:
                    for k in range(0, 2):
                        self.players[j].cardsInHand.append(self.deck[0])
                        self.deck.pop(0)
        
        for i in range(0, self.playerCount):
            self.players[i].cardsInHand = sortCards(self.players[i].cardsInHand)


    def throwCard(self, playerIndex):
        if self.players[playerIndex].cardsInHand == []:
            return 0
        card = self.players[playerIndex].decideCardToThrowOut(self)
        if card not in self.players[playerIndex].cardsInHand:
            index = -1
        else:
            index = self.players[playerIndex].cardsInHand.index(card)
        self.players[playerIndex].cardsInHand.pop(index)
        return card

        
    def takeCard(self, playerIndex):
        if self.deck != [] and self.thrownCards != []:
            self.players[playerIndex].setOptimalCards(self)
            tCard = self.thrownCards[-1]
            tmpGame = Game(2)
            tmpGame.players[1].cardsInHand = self.players[playerIndex].cardsInHand.copy()
            tmpGame.players[1].cardsInHand.append(tCard)
            tmpGame.players[1].setOptimalCards(tmpGame)
            thrownCardIsBetter = 0
            if tmpGame.players[1].isOpen == 0:
                if self.players[playerIndex].fEval < tmpGame.players[1].fEval and tmpGame.players[1].eval > 50:
                    cnt = 0
                    for slot in tmpGame.players[1].optimalCards:
                        for card in slot:
                            cnt += 1
                    if cnt < 15 and tmpGame.players[1].eval > 50 and ((tmpGame.players[0].danger > 3 and cnt > 7) or cnt == 14):
                        thrownCardIsBetter = 1
            else:
                if self.players[playerIndex].fEval < tmpGame.players[1].fEval:
                    thrownCardIsBetter = 1

            if thrownCardIsBetter == 1:
                self.players[playerIndex].cardsInHand.append(tCard)
                self.players[playerIndex].borrowedCard = tCard
                self.thrownCards.pop(-1)
                return

            if self.players[playerIndex].isOpen == 1 and len(self.players[playerIndex].cardsInHand) > 1:
                tCard = self.thrownCards[-1]
                for p in self.players:
                    for slot in p.cardsOnTable:
                        tmpLo = slot.copy()
                        tmpHi = slot.copy()
                        tmpLo.insert(0, tCard)
                        tmpHi.append(tCard)
                        
                        if ("W", "W", "1") in slot or ("W", "W", "2") in slot or ("W", "W", "3") in slot or ("W", "W", "4") in slot:
                            indexes = []
                            for card in slot:
                                if card[CARD_CLR] == "W":
                                    indexes.append(slot.index(card))
                            
                            for ind in indexes:
                                checkExit()
                                if ind == 0:
                                    if compareCards(tCard, slot[1], 1) == 2 and compareCards(tCard, slot[2], 1) == 1:
                                        self.players[playerIndex].cardsInHand.append(slot[ind])
                                        slot[ind] = tCard
                                        self.thrownCards.pop(-1)
                                        return
                                    if compareCards(tCard, slot[1], 1) == 2 and compareCards(tCard, slot[2], 1) == 2 and len(slot) == 4:
                                        self.players[playerIndex].cardsInHand.append(slot[ind])
                                        slot[ind] = tCard
                                        self.thrownCards.pop(-1)
                                        return
                                elif ind == len(slot) - 1:
                                    if compareCards(tCard, slot[-2], 1) == 2 and compareCards(tCard, slot[-3], 1) == 1:
                                        self.players[playerIndex].cardsInHand.append(slot[ind])
                                        slot[ind] = tCard
                                        self.thrownCards.pop(-1)
                                        return
                                    if compareCards(tCard, slot[-2], 1) == 2 and compareCards(tCard, slot[-3], 1) == 2 and len(slot) == 4:
                                        self.players[playerIndex].cardsInHand.append(slot[ind])
                                        slot[ind] = tCard
                                        self.thrownCards.pop(-1)
                                        return
                                else:
                                    if compareCards(tCard, slot[ind - 1], 1) == 2 and compareCards(tCard, slot[ind + 1], 1) == 2:
                                        if slot[ind - 1][CARD_CLR] != slot[ind + 1] and len == 4:
                                            self.players[playerIndex].cardsInHand.append(slot[ind])
                                            slot[ind] = tCard
                                            self.thrownCards.pop(-1)
                                            return
                                        else:
                                            self.players[playerIndex].cardsInHand.append(slot[ind])
                                            slot[ind] = tCard
                                            self.thrownCards.pop(-1)
                                            return

                        if tCard[CARD_CLR] == "W":
                            if candidateFlushOnTable(tmpHi) or candidateStraightFlushOnTable(tmpHi):
                                slot.append(tCard)
                                self.thrownCards.pop(-1)
                                return
                            if candidateStraightFlushOnTable(tmpLo):
                                slot.insert(0, tCard)
                                self.thrownCards.pop(-1)
                                return

                        else:
                            if candidateStraightFlushOnTable(tmpLo):
                                slot.insert(0, tCard)
                                self.thrownCards.pop(-1)
                                return
                            if candidateFlushOnTable(tmpHi) or candidateStraightFlushOnTable(tmpHi):
                                slot.append(tCard)
                                self.thrownCards.pop(-1)
                                return

            self.players[playerIndex].cardsInHand.append(self.deck[-1])
            self.deck.pop(-1)
        else:
            cards = self.thrownCards.copy()
            self.thrownCards = []
            self.deck = []
            while len(cards) != len(self.deck):
                checkExit()
                tmp = random.choice(cards)
                if tmp not in self.deck:
                    self.deck.append(tmp)
            
            if self.deck == []:
                cards = self.thrownCards.copy()
                self.thrownCards = []
                self.deck = []
                while len(cards) != len(self.deck):
                    checkExit()
                    tmp = random.choice(cards)
                    if tmp not in self.deck:
                        self.deck.append(tmp)
            
            self.players[playerIndex].cardsInHand.append(self.deck[-1])
            self.deck.pop(-1)

def humanTurn(game, screen, BLITS_DICT, ALL_CARD_BLITS, NUMBER_OF_PLAYERS):
    stayInGame = game.players[0].takeCard(game, Game(2), screen, BLITS_DICT, ALL_CARD_BLITS)
    if stayInGame == False:
        return True, -40
    displayBackground(screen, game, BLITS_DICT)
    displayPlayerCards(screen, NUMBER_OF_PLAYERS, ALL_CARD_BLITS, game, -1)
    displayPlayerButtons(screen, 1, BLITS_DICT)
    pygame.display.update()
    stayInGame = game.players[0].pickCard(game, screen, ALL_CARD_BLITS, BLITS_DICT)
    if stayInGame == False:
        return True, -40
    if stayInGame == 1:
        return False, -140
    if game.players[0].canOpen == 0:
        game.players[0].canOpen = 1
    return False, -40

def agentTurn(game, playerTurn, screen, BLITS_DICT, NUMBER_OF_PLAYERS, ALL_CARD_BLITS):
    winAmount = -40
    game.players[playerTurn].danger += 1
    formerLength = len(game.players[playerTurn].cardsInHand)
    time.sleep(0.5)
    
    if len(game.players[playerTurn].cardsInHand) < 15:
        game.takeCard(playerTurn)
        time.sleep(0.5)
    if checkExit2() == False:
        return True, winAmount
    
    game.players[playerTurn].setOptimalCards(game)
    if formerLength == 14 and len(game.players[playerTurn].cardsInHand) == 1:
        winAmount = -140
        return False, winAmount
    displayBackground(screen, game, BLITS_DICT)
    displayPlayerCards(screen, NUMBER_OF_PLAYERS, ALL_CARD_BLITS, game, -1)
    pygame.display.update()
    time.sleep(0.5)

    game.players[playerTurn].putCardsOnTable(game)
    if checkExit2() == False:
        return True, winAmount
    displayBackground(screen, game, BLITS_DICT)
    displayPlayerCards(screen, NUMBER_OF_PLAYERS, ALL_CARD_BLITS, game, -1)
    pygame.display.update()
    card = game.throwCard(playerTurn)
    if checkExit2() == False:
        return True, winAmount
    time.sleep(0.5)

    displayCardThrow(screen, card, game, playerTurn, ALL_CARD_BLITS, BLITS_DICT, 1)
    if checkExit2() == False:
        return True, winAmount
    if game.players[playerTurn].canOpen == 0:
        game.players[playerTurn].canOpen = 1
    return False, winAmount