import pygame
import tkinter as tk

root = tk.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X_UNIT = WIDTH // 16
Y_UNIT = HEIGHT // 9
CARD_WIDTH = X_UNIT + 2
CARD_HEIGHT = int(Y_UNIT * 1.5) + 2
CARD_CLR = 0
CARD_NMBR = 1
DEBUG = False

CARD_COLORS_DICT = {"♠": "_of_spades.png", "♥": "_of_hearts.png", "♣": "_of_clubs.png", "♦": "_of_diamonds.png", "W": "joker.png"}
CARD_NUMBERS_DICT = {"1": "ace",
                     "2": "2",
                     "3": "3",
                     "4": "4",
                     "5": "5",
                     "6": "6",
                     "7": "7",
                     "8": "8",
                     "9": "9",
                     "10": "10",
                     "J": "jack",
                     "Q": "queen",
                     "K": "king",
                     "W": ""}

PLAYER_INDEX_TO_START_POS = {"0": [X_UNIT * 5, HEIGHT - int(CARD_HEIGHT * 0.5)],
                             "1": [WIDTH - int(0.5 * X_UNIT), int(Y_UNIT * 6.5) - int(CARD_WIDTH * 0.5)],
                             "2": [X_UNIT * 10, 0 - int(CARD_HEIGHT * 0.5)],
                             "3": [0, int(Y_UNIT * 2.5) + int(CARD_WIDTH * 0.5)]}

PLAYER_INDEX_TO_END_POS = {"0": [X_UNIT * 10, HEIGHT - int(CARD_HEIGHT * 0.5)],
                           "1": [WIDTH - int(0.5 * X_UNIT), int(Y_UNIT * 2.5) + int(CARD_WIDTH * 0.5)],
                           "2": [X_UNIT * 5, 0 - int(CARD_HEIGHT * 0.5)],
                           "3": [0, int(Y_UNIT * 6.5) - int(CARD_WIDTH * 0.5)]}



SHADE_INDEX_TO_START_POS = {"0": [X_UNIT * 5 - 12, HEIGHT - int(CARD_HEIGHT * 0.5) - 12],
                             "1": [WIDTH - int(0.5 * X_UNIT) - 12, int(Y_UNIT * 6.5) - int(CARD_WIDTH * 0.5) + 12],
                             "2": [X_UNIT * 10 + 12, 0 - int(CARD_HEIGHT * 0.5) + 12],
                             "3": [12, int(Y_UNIT * 2.5) + int(CARD_WIDTH * 0.5) - 12]}

SHADE_INDEX_TO_END_POS = {"0": [X_UNIT * 10 + 12, HEIGHT - int(CARD_HEIGHT * 0.5) - 12],
                           "1": [WIDTH - int(0.5 * X_UNIT) - 12, int(Y_UNIT * 2.5) + int(CARD_WIDTH * 0.5) - 12],
                           "2": [X_UNIT * 5 - 12, 0 - int(CARD_HEIGHT * 0.5) + 12],
                           "3": [12, int(Y_UNIT * 6.5) - int(CARD_WIDTH * 0.5) + 12]}



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

THROWN_CARDS_POS = (WIDTH // 2 - CARD_WIDTH - 5, HEIGHT // 2 - int(0.65 * CARD_WIDTH))


def getInc(numberOfCards, xStartPos, yStartPos, xEndPos, yEndPos):
    if numberOfCards == 1:
        return (0, 0)
    x = (xEndPos - xStartPos) // (numberOfCards - 1)
    y = (yEndPos - yStartPos) // (numberOfCards - 1)
    if x > 1 * CARD_WIDTH:
        x = int(1 * CARD_WIDTH)
    if x < -1 * CARD_WIDTH:
        x = int(-1 * CARD_WIDTH)
    if y > 1 * CARD_HEIGHT:
        y = int(1 * CARD_HEIGHT)
    if y < -1 * CARD_HEIGHT:
        y = int(-1 * CARD_HEIGHT)
    return (x, y)
    

def blitRotateCenter(screen, image, x, y, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    screen.blit(rotated_image, new_rect)


def cardToImage(card):
    card_number = CARD_NUMBERS_DICT.get(card[CARD_NMBR])
    card_color = CARD_COLORS_DICT.get(card[CARD_CLR])
    return ".\\Card_gfx\\" + card_number + card_color


def displayThrownCard(screen, thrownCards):
    tmp = pygame.image.load(cardToImage(thrownCards[-1])).convert_alpha()
    tmp = pygame.transform.scale(tmp, (CARD_WIDTH, CARD_HEIGHT))
    cardDark = pygame.image.load(".\\Card_gfx\\card_dark.png").convert_alpha()
    cardDark = pygame.transform.scale(cardDark, (CARD_WIDTH, CARD_HEIGHT))
    x, y = THROWN_CARDS_POS[0], THROWN_CARDS_POS[1]
    for card in thrownCards:
        screen.blit(cardDark, (int(x), int(y)))
        y -= 0.2
        x -= 0.15
    screen.blit(tmp, (int(x), int(y)))


# ---------------------------------------------------------------------------------------------------------------------------


def displayLeaderboard(screen, game):
    font = pygame.font.Font('freesansbold.ttf', 15)
    xPos = int(X_UNIT * 1.5)
    yPos = 30
    length = len(game.players)
    for i in range(0, length):
        if i == 0:
            text = font.render('Player ', True, (255, 255, 255))
        else:
            text = font.render('Agent ' + str(i), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (xPos, yPos)
        screen.blit(text, textRect)
        xPos += int(0.75 * X_UNIT)
    yPos += int(Y_UNIT * 0.5)
    if (game.leaderboard) != []:
        row = game.leaderboard[-1]
        xPos = int(X_UNIT * 1.5)
        for pSum in row:
            text = font.render(str(pSum), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (xPos, yPos)
            screen.blit(text, textRect)
            xPos += int(0.75 * X_UNIT)
    text = font.render("Round " + str(game.round), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (int(X_UNIT * 0.5), 30)
    screen.blit(text, textRect)



def displayPlayerButtons(screen, state, BLITS_DICT):
    button = BLITS_DICT["miniButton"]
    font = pygame.font.Font('freesansbold.ttf', 15)
    if state == 1:
        text = font.render('Throw a card', True, (255, 255, 255))
    else:
        text = font.render('Finish/Cancel', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH - CARD_WIDTH, HEIGHT - int(0.25 * Y_UNIT))
    screen.blit(button, (WIDTH - CARD_WIDTH - X_UNIT, HEIGHT - int(0.5 * Y_UNIT)))
    screen.blit(text, textRect)

    if state == 1:
        text = font.render('Choose cards to put down', True, (255, 255, 255))
    else:
        text = font.render('Put selected cards down', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH - CARD_WIDTH, HEIGHT  - int(0.75 * Y_UNIT))
    screen.blit(button, (WIDTH - CARD_WIDTH - X_UNIT, HEIGHT - Y_UNIT))
    screen.blit(text, textRect)
    text = font.render('Auto-set', True, (255, 255, 255))
    textRect = text.get_rect()
    screen.blit(button, (WIDTH - CARD_WIDTH - X_UNIT, HEIGHT - int(1.5 * Y_UNIT)))
    textRect.center = (WIDTH - CARD_WIDTH, HEIGHT  - int(1.25 * Y_UNIT))
    screen.blit(text, textRect)
    pygame.display.update()



def displayCardShades(screen, numberOfPlayers, game, shade):
    for p in range(0, numberOfPlayers):
        playerIndex = str(p)
        if p == 1 and numberOfPlayers == 2:
            playerIndex = "2"
        posX = SHADE_INDEX_TO_START_POS[playerIndex][0]
        posY = SHADE_INDEX_TO_START_POS[playerIndex][1]
        playerCards = game.players[p].cardsInHand.copy()
        length = len(playerCards)
        if length == 1:
            if playerIndex == "1" or playerIndex == "3":
                blitRotateCenter(screen, shade, posX + int(0.25 * CARD_WIDTH), posY - int(0.25), 90)
            else:
                screen.blit(shade, (posX, posY))
        else:
            for i in range(0, length):
                if playerIndex == "0" or playerIndex == "2":
                    screen.blit(shade, (posX, posY))
                else:
                    blitRotateCenter(screen, shade, posX + int(0.25 * CARD_WIDTH), posY - int(0.25), 90)

                    
                posX += getInc(len(playerCards), SHADE_INDEX_TO_START_POS[playerIndex][0], SHADE_INDEX_TO_START_POS[playerIndex][1], SHADE_INDEX_TO_END_POS[playerIndex][0], SHADE_INDEX_TO_END_POS[playerIndex][1])[0]
                posY += getInc(len(playerCards), SHADE_INDEX_TO_START_POS[playerIndex][0], SHADE_INDEX_TO_START_POS[playerIndex][1], SHADE_INDEX_TO_END_POS[playerIndex][0], SHADE_INDEX_TO_END_POS[playerIndex][1])[1]



def displayBackground(screen, game, BLITS_DICT):
    bg = BLITS_DICT["bg"]
    back = BLITS_DICT["back"]
    backDark = BLITS_DICT["backDark"]
    shade = BLITS_DICT["shade"]
    menuButton = BLITS_DICT["menuButton"]
    screen.blit(bg, (0, 0))
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('x', True, (255, 255, 255))
    screen.blit(menuButton, (WIDTH - 60, 10))
    textRect = text.get_rect()
    textRect.center = (WIDTH - 20, 20)
    screen.blit(text, textRect)
    if game.deck != []:
        x, y = THROWN_CARDS_POS[0] + CARD_WIDTH + 5, THROWN_CARDS_POS[1]
        for card in game.deck:
            screen.blit(backDark, (int(x), int(y)))
            y -= 0.2
            x += 0.15
        screen.blit(back, (int(x), int(y)))
    displayLeaderboard(screen, game)
    if game.thrownCards != []:
        displayThrownCard(screen, game.thrownCards)
    displayCardShades(screen, len(game.players), game, shade)



def displayVictory(screen, game, BLITS_DICT, playerIndex, blitDict, roundOrGame):
    displayBackground(screen, game, BLITS_DICT)
    displayPlayerCards(screen, len(game.players), blitDict, game, -1)
    font = pygame.font.Font('freesansbold.ttf', 20)
    if roundOrGame == 0:
        if str(playerIndex) == "0":
            text = font.render("Player won this round!", True, (255, 255, 255), (0, 0, 0))
        else:
            text = font.render("Agent " + str(playerIndex) + " won this round!", True, (255, 255, 255), (0, 0, 0))
    else:
        if str(playerIndex) == "0":
            text = font.render("Player won the game!", True, (255, 255, 255), (0, 0, 0))
        else:
            text = font.render("Agent " + str(playerIndex) + " won the game!", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)
    pygame.display.update()
    


def displayCardsOnTable(screen, game, playerIndex, blitDict):
    length = len(game.players[playerIndex].cardsOnTable)
    cardPosIndex = playerIndex
    if len(game.players) == 2 and playerIndex == 1:
        cardPosIndex = 2
    for i in range(0, length):
        posX = TABLE_CARDS_START_POS[str(cardPosIndex) + str(i)][0]
        posY = TABLE_CARDS_START_POS[str(cardPosIndex) + str(i)][1]
        xEndPos = TABLE_CARDS_END_POS[str(cardPosIndex) + str(i)][0]
        yEndPos = TABLE_CARDS_END_POS[str(cardPosIndex) + str(i)][1]
        incX = getInc(len(game.players[playerIndex].cardsOnTable[i]) + 1, posX, posY, xEndPos, yEndPos)[0]
        incY = getInc(len(game.players[playerIndex].cardsOnTable[i]) + 1, posX, posY, xEndPos, yEndPos)[1]
        for card in game.players[playerIndex].cardsOnTable[i]:
            index = game.cards.index(card)
            if cardPosIndex == 1:
                blitRotateCenter(screen, blitDict[index], posX + int(0.25 * CARD_WIDTH), posY - int(0.25), -90)
            elif cardPosIndex == 3:
                blitRotateCenter(screen, blitDict[index], posX + int(0.25 * CARD_WIDTH), posY - int(0.25), -90)
            else:
                screen.blit(blitDict[index], (posX, posY))
            posX += incX
            if cardPosIndex == 1:
                continue
            posY += incY



def displayPlayerCards(screen, numberOfPlayers, blitDict, game, chosenCard):
    back = pygame.image.load(".\\Card_gfx\\card_back.png").convert_alpha()
    back = pygame.transform.scale(back, (CARD_WIDTH, CARD_HEIGHT))
    for p in range(0, numberOfPlayers):
        displayCardsOnTable(screen, game, p, blitDict)
        playerIndex = str(p)
        if p == 1 and numberOfPlayers == 2:
            playerIndex = "2"
        posX = PLAYER_INDEX_TO_START_POS[playerIndex][0]
        posY = PLAYER_INDEX_TO_START_POS[playerIndex][1]
        playerCards = game.players[p].cardsInHand.copy()
        length = len(playerCards)
        if length == 1:
            index = game.cards.index(playerCards[0])
            if playerIndex == "1" or playerIndex == "3":
                if DEBUG:
                    blitRotateCenter(screen, blitDict[index], posX + int(0.25 * CARD_WIDTH), posY - int(0.25), 90)
                else:
                    blitRotateCenter(screen, back, posX + int(0.25 * CARD_WIDTH), posY - int(0.25), 90)
            else:
                if DEBUG or p == 0:
                    screen.blit(blitDict[index], (posX, posY))
                else:
                    screen.blit(back, (posX, posY))
        else:
            for i in range(0, length):
                index = game.cards.index(playerCards[i])
                if playerIndex == "0":
                    if i == chosenCard:
                        screen.blit(blitDict[index], (posX, posY - 5))
                    else:
                        screen.blit(blitDict[index], (posX, posY))
                elif playerIndex == "2":
                    if DEBUG:
                        screen.blit(blitDict[index], (posX, posY))
                    else:
                        screen.blit(back, (posX, posY))
                else:
                    if DEBUG:
                        blitRotateCenter(screen, blitDict[index], posX + int(0.25 * CARD_WIDTH), posY - int(0.25), 90)
                    else:
                        blitRotateCenter(screen, back, posX + int(0.25 * CARD_WIDTH), posY - int(0.25), 90)

                    
                posX += getInc(len(playerCards), PLAYER_INDEX_TO_START_POS[playerIndex][0], PLAYER_INDEX_TO_START_POS[playerIndex][1], PLAYER_INDEX_TO_END_POS[playerIndex][0], PLAYER_INDEX_TO_END_POS[playerIndex][1])[0]
                posY += getInc(len(playerCards), PLAYER_INDEX_TO_START_POS[playerIndex][0], PLAYER_INDEX_TO_START_POS[playerIndex][1], PLAYER_INDEX_TO_END_POS[playerIndex][0], PLAYER_INDEX_TO_END_POS[playerIndex][1])[1]
        


def displayPlayerCards2(screen, numberOfPlayers, blitDict, game, chosenCardsTable):
    back = pygame.image.load(".\\Card_gfx\\card_back.png").convert_alpha()
    back = pygame.transform.scale(back, (CARD_WIDTH, CARD_HEIGHT))
    for p in range(0, numberOfPlayers):
        displayCardsOnTable(screen, game, p, blitDict)
        playerIndex = str(p)
        if p == 1 and numberOfPlayers == 2:
            playerIndex = "2"
        posX = PLAYER_INDEX_TO_START_POS[playerIndex][0]
        posY = PLAYER_INDEX_TO_START_POS[playerIndex][1]
        playerCards = game.players[p].cardsInHand.copy()
        length = len(playerCards)
        if length == 1:
            index = game.cards.index(playerCards[0])
            if playerIndex == "1" or playerIndex == "3":
                if DEBUG:
                    rotated_image = pygame.transform.rotate(blitDict[index], 90)
                    new_rect = rotated_image.get_rect(center = blitDict[index].get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                    screen.blit(rotated_image, new_rect)
                else:
                    rotated_image = pygame.transform.rotate(back, 90)
                    new_rect = rotated_image.get_rect(center = back.get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                    screen.blit(rotated_image, new_rect)
            else:
                if DEBUG or p == 0:
                    screen.blit(blitDict[index], (posX, posY))
                else:
                    screen.blit(back, (posX, posY))
        else:
            for i in range(0, length):
                index = game.cards.index(playerCards[i])
                if playerIndex == "0":
                    if i in chosenCardsTable:
                        screen.blit(blitDict[index], (posX, posY - 5))
                    else:
                        screen.blit(blitDict[index], (posX, posY))
                elif playerIndex == "2":
                    if DEBUG:
                        screen.blit(blitDict[index], (posX, posY))
                    else:
                        screen.blit(back, (posX, posY))
                else:
                    if DEBUG:
                        rotated_image = pygame.transform.rotate(blitDict[index], 90)
                        new_rect = rotated_image.get_rect(center = blitDict[index].get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                        screen.blit(rotated_image, new_rect)
                    else:
                        rotated_image = pygame.transform.rotate(back, 90)
                        new_rect = rotated_image.get_rect(center = back.get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                        screen.blit(rotated_image, new_rect)

                    
                posX += getInc(len(playerCards), PLAYER_INDEX_TO_START_POS[playerIndex][0], PLAYER_INDEX_TO_START_POS[playerIndex][1], PLAYER_INDEX_TO_END_POS[playerIndex][0], PLAYER_INDEX_TO_END_POS[playerIndex][1])[0]
                posY += getInc(len(playerCards), PLAYER_INDEX_TO_START_POS[playerIndex][0], PLAYER_INDEX_TO_START_POS[playerIndex][1], PLAYER_INDEX_TO_END_POS[playerIndex][0], PLAYER_INDEX_TO_END_POS[playerIndex][1])[1]



def displayCardThrow(screen, card, game, playerIndex, blitDict, BLITS_DICT, toAppend):
    if card == 0:
        return
    if len(game.players) == 2 and playerIndex == 1:
        playerIndex = 2
    playerIndex = str(playerIndex)
    posX = PLAYER_INDEX_TO_START_POS[playerIndex][0]
    posY = PLAYER_INDEX_TO_START_POS[playerIndex][1]
    for i in range(0, 9):
        displayBackground(screen, game, BLITS_DICT)
        tmp = pygame.image.load(cardToImage(card)).convert_alpha()
        tmp = pygame.transform.scale(tmp, (CARD_WIDTH, CARD_HEIGHT))
        displayPlayerCards(screen, len(game.players), blitDict, game, -1)
        screen.blit(tmp, (posX, posY))
        pygame.display.update()
        posX += getInc(10, PLAYER_INDEX_TO_START_POS[playerIndex][0], PLAYER_INDEX_TO_START_POS[playerIndex][1], THROWN_CARDS_POS[0], THROWN_CARDS_POS[1])[0]
        posY += getInc(10, PLAYER_INDEX_TO_START_POS[playerIndex][0], PLAYER_INDEX_TO_START_POS[playerIndex][1], THROWN_CARDS_POS[0], THROWN_CARDS_POS[1])[1]

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    if toAppend == 1:
        game.thrownCards.append(card)
    displayBackground(screen, game, BLITS_DICT)
    displayPlayerCards(screen, len(game.players), blitDict, game, -1)