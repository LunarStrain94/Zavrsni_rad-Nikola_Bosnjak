import random
from CheckCandidates import *
from Player import *

class Game:
    def __init__(self, playerCount):
        self.playerCount = playerCount # Postavljanje igraca i leaderboarda
        self.leaderboard = []
        self.players = []
        for i in range(0, playerCount): # ODKOMENTIRAT POSLE
            if i == 0:
                self.players.append(Human([])) # Pretpostavimo da je ljudski igrac uvijek Player 0
            else:
                self.players.append(Agent([]))
        colors = ["♠", "♥", "♣", "♦"] # Postavljanje (nepromjesanog) spila
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        self.deck = []
        for c in colors:
            for n in numbers:
                self.cards.append((c, n, "1"))
                self.cards.append((c, n, "2"))
        for i in range(0, 4):
            self.cards.append(("W", "W", str(i + 1))) # W = wildcard, iliti Joker
        self.thrownCards = [] # Vrh spila = indeks 0 od deck. 
                              # Provjeriti jel moguc append na prvo mjesto zbog konzistentnosti,
                              # ako ne, najvisa bacena karta je na -1

    def shuffle(self, dealer): # Mjesanje i dijeljenje, dealer predstavlja indeks igraca koji dijeli, 
        cards = self.cards.copy() # u listi self.players[]
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
            self.players[i].danger = 0
            self.players[i].isOpen = 0

        for i in range(0, 7):
            for j in range(dealer - self.playerCount + 1, dealer + 1): # Koriste se indeksi u minusu da se pristupi
                if i == 0 and dealer - self.playerCount + 1 == j: # igracima bez da im se mijenja raspored u listi
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
        card = self.players[playerIndex].decideCardToThrowOut(self)
        index =  self.players[playerIndex].cardsInHand.index(card)
        self.players[playerIndex].cardsInHand.pop(index)
        return card

        
    def takeCard(self, playerIndex):
        if self.deck != [] and self.thrownCards:
            self.players[playerIndex].setOptimalCards(self)
            tmpPlayer = Agent(self.players[playerIndex].cardsInHand.copy())
            tmpPlayer.cardsInHand.append(self.thrownCards[-1])
            tmpPlayer.setOptimalCards(self)
            #thrownCardIsBetter = 0
            #if len(tmpPlayer.optimalCards) > len(self.players[playerIndex].cardsInHand):
            #    if len(tmpPlayer.optimalCards) < 15:
            #        thrownCardIsBetter = 1

            #if thrownCardIsBetter == 1:
            #    if self.players[playerIndex].eval < tmpPlayer.eval and self.players[playerIndex].danger > 14:
            #        self.players[playerIndex].cardsInHand.append(self.thrownCards[-1])
            #        self.thrownCards.pop(-1)
            #    elif self.players[playerIndex].eval < tmpPlayer.eval and len(tmpPlayer.optimalCards) == 14:
            #        self.players[playerIndex].cardsInHand.append(self.thrownCards[-1])
            #        self.thrownCards.pop(-1)
            #    elif self.players[playerIndex].isOpen == 1:
            #        self.players[playerIndex].cardsInHand.append(self.thrownCards[-1])
            #        self.thrownCards.pop(-1)
            #    else:
            #        self.players[playerIndex].cardsInHand.append(self.deck[-1])
            #        self.deck.pop(-1)
            #else:
            self.players[playerIndex].cardsInHand.append(self.deck[-1])
            self.deck.pop(-1)
        else:
            cards = self.thrownCards.copy()
            self.thrownCards = []
            self.deck = []
            while len(cards) != len(self.deck):
                tmp = random.choice(cards)
                if tmp not in self.deck:
                    self.deck.append(tmp)


            self.players[playerIndex].cardsInHand.append(self.deck[-1])
            self.deck.pop(-1)