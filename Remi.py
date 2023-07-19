import pygame
from Game import *
from CheckCandidates import *
from Evaluation import *
from Display import *
import tkinter as tk
import time
#import cProfile

#def test():
root = tk.Tk()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Remi')

back = pygame.image.load(".\\Card_gfx\\card_back.png").convert_alpha()
back = pygame.transform.scale(back, (CARD_WIDTH, CARD_HEIGHT))
bg = pygame.image.load(".\\Card_gfx\\bg.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

ALL_CARDS_BLIT_DICT = []
NUMBER_OF_PLAYERS = 4
game = Game(NUMBER_OF_PLAYERS)
for card in game.cards:
    tmp = pygame.image.load(cardToImage(card)).convert_alpha()
    tmp = pygame.transform.scale(tmp, (CARD_WIDTH, CARD_HEIGHT))
    ALL_CARDS_BLIT_DICT.append(tmp)

running = True
initialising = True
inMenu = True
inGame = True

while running:
    if inMenu:
        NUMBER_OF_PLAYERS = mainMenu(screen, bg)

    while initialising:
        dealer = random.randint(0, NUMBER_OF_PLAYERS - 1)
        game = Game(NUMBER_OF_PLAYERS)
        game.shuffle(dealer)
        playerTurn = (dealer + 1) % NUMBER_OF_PLAYERS
        break

    while inGame:
        print(len(game.players))
        inRound = True
        winnerInd = -1
        winAmount = -40
        roundCnt = 0
        while inRound:
            displayBackground(screen, game, bg, back)
            displayPlayerCards(screen, NUMBER_OF_PLAYERS, ALL_CARDS_BLIT_DICT, game, -1)
            pygame.display.update()

            if playerTurn == 0:
                game.players[0].takeCard(game)
                displayBackground(screen, game, bg, back)
                displayPlayerCards(screen, NUMBER_OF_PLAYERS, ALL_CARDS_BLIT_DICT, game, -1)
                displayPlayerButtons(screen, 1)
                pygame.display.update()
                game.players[0].pickCard(game, screen, ALL_CARDS_BLIT_DICT, bg, back)
            else:
                game.players[playerTurn].danger += 1
                tmpLength = len(game.players[playerTurn].cardsInHand)
                time.sleep(0.5)
                if len(game.players[playerTurn].cardsInHand) < 15:
                    game.takeCard(playerTurn)
                    time.sleep(0.5)
                game.players[playerTurn].setOptimalCards(game)
                if tmpLength == 14 and len(game.players[playerTurn].cardsInHand) == 1:
                    winAmount = -140
                displayBackground(screen, game, bg, back)
                displayPlayerCards(screen, NUMBER_OF_PLAYERS, ALL_CARDS_BLIT_DICT, game, -1)
                pygame.display.update()
                time.sleep(0.5)
                game.players[playerTurn].putCardsOnTable(game)
                displayBackground(screen, game, bg, back)
                displayPlayerCards(screen, NUMBER_OF_PLAYERS, ALL_CARDS_BLIT_DICT, game, -1)
                pygame.display.update()
                card = game.throwCard(playerTurn)
                time.sleep(0.5)
                displayCardThrow(screen, card, game, playerTurn, ALL_CARDS_BLIT_DICT, bg, back, 1)

            pygame.display.update()
            if len(game.players[playerTurn].cardsInHand) == 0:
                roundCnt += 1
                winnerInd = playerTurn
                displayVictory(screen, game, bg, back, playerTurn, ALL_CARDS_BLIT_DICT, 0)
                time.sleep(5)
                inRound = False
                break

            playerTurn += 1
            if playerTurn >= NUMBER_OF_PLAYERS:
                playerTurn -= NUMBER_OF_PLAYERS
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        
        tmp = []
        for i in range(0, NUMBER_OF_PLAYERS):
            if i == winnerInd:
                tmp.append(winAmount)
            elif len(game.players[i].cardsInHand) == 14:
                if winAmount == -140:
                    tmp.append(200)
                else:
                    tmp.append(100)
            else:
                pSum = 0
                for card in game.players[i].cardsInHand:
                    if card[CARD_CLR] == "W":
                        pSum += 25
                    else:
                        pSum += toValue(card[CARD_NMBR])
                if winAmount == -140:
                    tmp.append(round(pSum/10)*10 * 2)
                else:
                    tmp.append(round(pSum/10)*10)
            
        if roundCnt == NUMBER_OF_PLAYERS * 4:
            ingame = False
            minSum = 1000
            minInd = -1
            for playerSum in game.leaderboard[-1]:
                if playerSum < minSum:
                    minSum = playerSum
                    minInd = game.leaderboard[-1].index(playerSum)
            displayVictory(screen, game, bg, back, playerTurn, ALL_CARDS_BLIT_DICT, 1)
            time.sleep(5)
            inMenu = True
            break

        game.leaderboard.append(tmp)
        if len(game.leaderboard) > 1:
            for p in range(0, NUMBER_OF_PLAYERS):
                game.leaderboard[-1][p] += game.leaderboard[-2][p]
       
        dealer = (dealer + 1) % NUMBER_OF_PLAYERS
        playerTurn = (dealer + 1) % NUMBER_OF_PLAYERS
        game.shuffle(dealer)

            

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
