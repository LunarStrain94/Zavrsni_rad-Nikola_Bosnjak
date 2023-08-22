import pygame
from Game import *
from CheckCandidates import *
from Evaluation import *
from Display import *
import tkinter as tk
import time

root = tk.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X_UNIT = WIDTH // 16
Y_UNIT = HEIGHT // 9
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Remi')

highlight = pygame.image.load(".\\Card_gfx\\card_highlight.png").convert_alpha()
highlight = pygame.transform.scale(highlight, (CARD_WIDTH, CARD_HEIGHT))
back = pygame.image.load(".\\Card_gfx\\card_back.png").convert_alpha()
back = pygame.transform.scale(back, (CARD_WIDTH, CARD_HEIGHT))
backDark = pygame.image.load(".\\Card_gfx\\card_back_dark.png").convert_alpha()
backDark = pygame.transform.scale(backDark, (CARD_WIDTH, CARD_HEIGHT))
bg = pygame.image.load(".\\Card_gfx\\bg.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
shade = pygame.image.load(".\\Card_gfx\\card_shade.png").convert_alpha()
shade = pygame.transform.scale(shade, (CARD_WIDTH, CARD_HEIGHT))
button = pygame.image.load(".\\Card_gfx\\button.png").convert_alpha()
button = pygame.transform.scale(button, (4 * X_UNIT, Y_UNIT))
miniButton = pygame.image.load(".\\Card_gfx\\button.png").convert_alpha()
miniButton = pygame.transform.scale(miniButton, (2 * X_UNIT, int(0.5 * Y_UNIT) - 4))
menuButton = pygame.image.load(".\\Card_gfx\\menu_button.png").convert_alpha()
menuButton = pygame.transform.scale(menuButton, (20, 20))

BLITS_DICT = {"bg": bg, "back": back, "backDark": backDark, "shade": shade, "highlight": highlight, "button": button, "miniButton": miniButton, "menuButton": menuButton}
ALL_CARD_BLITS = []
NUMBER_OF_PLAYERS = 4
game = Game(NUMBER_OF_PLAYERS)
for card in game.cards:
    tmp = pygame.image.load(cardToImage(card)).convert_alpha()
    tmp = pygame.transform.scale(tmp, (CARD_WIDTH, CARD_HEIGHT))
    ALL_CARD_BLITS.append(tmp)

running = True
inMenu = True

while running:
    if inMenu:
        NUMBER_OF_PLAYERS = mainMenu(screen, BLITS_DICT)
        initialising = True
        inGame = True

    if initialising:
        dealer = random.randint(0, NUMBER_OF_PLAYERS - 1)
        game = Game(NUMBER_OF_PLAYERS)
        game.shuffle(dealer)
        playerTurn = (dealer + 1) % NUMBER_OF_PLAYERS

    while inGame:
        inRound = True
        winnerInd = -1
        winAmount = -40
        while inRound:
            displayBackground(screen, game, BLITS_DICT)
            displayPlayerCards(screen, NUMBER_OF_PLAYERS, ALL_CARD_BLITS, game, -1)
            if playerTurn == 0:
                y = len(game.deck) * 0.2
                x = len(game.deck) * 0.15
                screen.blit(highlight, (WIDTH // 2 + int(x), HEIGHT // 2 - int(0.65 * CARD_WIDTH + y)))
            pygame.display.update()

            if playerTurn == 0:
                toMenu, winAmount = humanTurn(game, screen, BLITS_DICT, ALL_CARD_BLITS, NUMBER_OF_PLAYERS)
                if toMenu:
                    inRound = False
                    inGame = False
                    break
            else:
                toMenu, winAmount = agentTurn(game, playerTurn, screen, BLITS_DICT, NUMBER_OF_PLAYERS, ALL_CARD_BLITS)
                if toMenu:
                    inRound = False
                    inGame = False
                    break
            pygame.display.update()
            if checkExit2() == False:
                inRound = False
                inGame = False
                break

            if len(game.players[playerTurn].cardsInHand) == 0:
                winnerInd = playerTurn
                displayVictory(screen, game, BLITS_DICT, playerTurn, ALL_CARD_BLITS, 0)
                time.sleep(5)
                game.round += 1
                inRound = False
                break
            playerTurn += 1
            if playerTurn >= NUMBER_OF_PLAYERS:
                playerTurn -= NUMBER_OF_PLAYERS
            pygame.display.update()
        

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
            
        if game.round == NUMBER_OF_PLAYERS * 4 + 1:
            ingame = False
            minSum = 1000
            minInd = -1
            for playerSum in game.leaderboard[-1]:
                if playerSum < minSum:
                    minSum = playerSum
                    minInd = game.leaderboard[-1].index(playerSum)
            displayVictory(screen, game, BLITS_DICT, playerTurn, ALL_CARD_BLITS, 1)
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