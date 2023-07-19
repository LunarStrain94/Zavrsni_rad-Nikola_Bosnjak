import pygame
import tkinter as tk

root = tk.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight() - 60
CARD_WIDTH = WIDTH // 16
CARD_HEIGHT = int(HEIGHT // 9 * 1.5)
CARD_CLR = 0
CARD_NMBR = 1
DEBUG = True

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


def getInc(numberOfCards, xStartPos, yStartPos, xEndPos, yEndPos):
    if numberOfCards == 1:
        return (0, 0)
    x = (xEndPos - xStartPos) // (numberOfCards - 1)
    y = (yEndPos - yStartPos) // (numberOfCards - 1)
    if x > 0.5 * CARD_WIDTH:
        x = int(0.5 * CARD_WIDTH)
    if x < -0.5 * CARD_WIDTH:
        x = int(-0.5 * CARD_WIDTH)
    if y > 0.5 * CARD_HEIGHT:
        y = int(0.5 * CARD_HEIGHT)
    if y < -0.5 * CARD_HEIGHT:
        y = int(-0.5 * CARD_HEIGHT)
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
    screen.blit(tmp, THROWN_CARDS_POS)


# ---------------------------------------------------------------------------------------------------------------------------


def mainMenu(screen, bg):
    screen.blit(bg, (0, 0))
    font = pygame.font.Font('freesansbold.ttf', 40)
    xPos = WIDTH // 2
    yPos = HEIGHT // 4
    text = font.render('Remi', True, (255, 255, 255))
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
        text = font.render("Play with " + str(i) + " player" + s, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (xPos, yPos)
        screen.blit(text, textRect)
        buttonCoords.append([xPos - WIDTH // 8, yPos - HEIGHT // 16, xPos + WIDTH // 8, yPos + HEIGHT // 16])
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
                
            if mousePos != (-1, -1):
                for pos in buttonCoords:
                    if mousePos[0] >= pos[0] and mousePos[0] <= pos[2] and mousePos[1] >= pos[1] and mousePos[1] <= pos[3]:
                       return (buttonCoords.index(pos) + 2)


def displayLeaderboard(screen, game):
    font = pygame.font.Font('freesansbold.ttf', 15)
    xPos = WIDTH // 32
    yPos = HEIGHT // 18
    length = len(game.players)
    for i in range(0, length):
        text = font.render('Player ' + str(i), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (xPos, yPos)
        screen.blit(text, textRect)
        xPos += WIDTH // 16
    yPos += HEIGHT // 18
    for row in game.leaderboard:
        xPos = WIDTH // 32
        for pSum in row:
            text = font.render(str(pSum), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (xPos, yPos)
            screen.blit(text, textRect)
            xPos += WIDTH // 16


def displayPlayerButtons(screen, state):
    font = pygame.font.Font('freesansbold.ttf', 15)
    if state == 1:
        text = font.render('Throw card', True, (255, 255, 255), (0, 0, 0))
    else:
        text = font.render('Cancel', True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH - CARD_WIDTH, HEIGHT - int(0.5 * CARD_HEIGHT))
    screen.blit(text, textRect)

    if state == 1:
        text = font.render('Choose cards to put down', True, (255, 255, 255), (0, 0, 0))
    else:
        text = font.render('Put down', True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH - CARD_WIDTH, HEIGHT - int(1 * CARD_HEIGHT))
    screen.blit(text, textRect)
    pygame.display.update()


def displayBackground(screen, game, bg, back):
    screen.blit(bg, (0, 0))
    if game.deck != []:
        screen.blit(back, (WIDTH // 2 + 2 * CARD_WIDTH, HEIGHT // 2 - int(0.65 * CARD_WIDTH)))
    displayLeaderboard(screen, game)
    if game.thrownCards != []:
        displayThrownCard(screen, game.thrownCards)


def displayVictory(screen, game, bg, back, playerIndex, blitDict, roundOrGame):
    displayBackground(screen, game, bg, back)
    displayPlayerCards(screen, len(game.players), blitDict, game, -1)
    font = pygame.font.Font('freesansbold.ttf', 20)
    if roundOrGame == 0:
        text = font.render("Player " + str(playerIndex) + " won this round!", True, (255, 255, 255), (0, 0, 0))
    else:
        text = font.render("Player " + str(playerIndex) + " won the game!", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)
    pygame.display.update()
    

def displayCardsOnTable(screen, game, playerIndex, blitDict):
    length = len(game.players[playerIndex].cardsOnTable)
    if len(game.players) == 2 and playerIndex == 1:
        playerIndex = 2
    for i in range(0, length):
        posX = TABLE_CARDS_START_POS[str(playerIndex) + str(i)][0]
        posY = TABLE_CARDS_START_POS[str(playerIndex) + str(i)][1]
        xEndPos = TABLE_CARDS_END_POS[str(playerIndex) + str(i)][0]
        yEndPos = TABLE_CARDS_END_POS[str(playerIndex) + str(i)][1]
        incX = getInc(len(game.players[playerIndex].cardsOnTable[i]) + 1, posX, posY, xEndPos, yEndPos)[0]
        incY = getInc(len(game.players[playerIndex].cardsOnTable[i]) + 1, posX, posY, xEndPos, yEndPos)[1]
        for card in game.players[playerIndex].cardsOnTable[i]:
            index = game.cards.index(card)
            if playerIndex == 1:
                rotated_image = pygame.transform.rotate(blitDict[index], -90)
                new_rect = rotated_image.get_rect(center = blitDict[index].get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                screen.blit(rotated_image, new_rect)
            elif playerIndex == 3:
                rotated_image = pygame.transform.rotate(blitDict[index], 90)
                new_rect = rotated_image.get_rect(center = blitDict[index].get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                screen.blit(rotated_image, new_rect)
            else:
                screen.blit(blitDict[index], (posX, posY))
            posX += incX
            if playerIndex == 1: # Ne mogu pronaći grešku u koordinatama, pa nek ovo za sad stoji
                continue
            posY += incY


def displayPlayerCards(screen, numberOfPlayers, blitDict, game, chosenCard):
    back = pygame.image.load(".\\Card_gfx\\card_back.png").convert_alpha()
    back = pygame.transform.scale(back, (CARD_WIDTH, CARD_HEIGHT))
    for p in range(0, numberOfPlayers):
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
                rotated_image = pygame.transform.rotate(blitDict[index], 90)
                new_rect = rotated_image.get_rect(center = blitDict[index].get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                screen.blit(rotated_image, new_rect)
            else:
                screen.blit(blitDict[index], (posX, posY))
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
                        rotated_image = pygame.transform.rotate(blitDict[index], 90)
                        new_rect = rotated_image.get_rect(center = blitDict[index].get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                        screen.blit(rotated_image, new_rect)
                    else:
                        rotated_image = pygame.transform.rotate(back, 90)
                        new_rect = rotated_image.get_rect(center = back.get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                        screen.blit(rotated_image, new_rect)

                    
                posX += getInc(len(playerCards), PLAYER_INDEX_TO_START_POS[playerIndex][0], PLAYER_INDEX_TO_START_POS[playerIndex][1], PLAYER_INDEX_TO_END_POS[playerIndex][0], PLAYER_INDEX_TO_END_POS[playerIndex][1])[0]
                posY += getInc(len(playerCards), PLAYER_INDEX_TO_START_POS[playerIndex][0], PLAYER_INDEX_TO_START_POS[playerIndex][1], PLAYER_INDEX_TO_END_POS[playerIndex][0], PLAYER_INDEX_TO_END_POS[playerIndex][1])[1]
        displayCardsOnTable(screen, game, p, blitDict)


def displayPlayerCards2(screen, numberOfPlayers, blitDict, game, chosenCardsTable):
    back = pygame.image.load(".\\Card_gfx\\card_back.png").convert_alpha()
    back = pygame.transform.scale(back, (CARD_WIDTH, CARD_HEIGHT))
    for p in range(0, numberOfPlayers):
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
                rotated_image = pygame.transform.rotate(blitDict[index], 90)
                new_rect = rotated_image.get_rect(center = blitDict[index].get_rect(center = (posX + int(0.25 * CARD_WIDTH), posY - int(0.25))).center)
                screen.blit(rotated_image, new_rect)
            else:
                screen.blit(blitDict[index], (posX, posY))
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
        displayCardsOnTable(screen, game, p, blitDict)


def displayCardThrow(screen, card, game, playerIndex, blitDict, bg, back, toAppend):
    playerIndex = str(playerIndex)
    posX = PLAYER_INDEX_TO_START_POS[playerIndex][0]
    posY = PLAYER_INDEX_TO_START_POS[playerIndex][1]
    for i in range(0, 9):
        displayBackground(screen, game, bg, back)
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
    displayBackground(screen, game, bg, back)
    displayPlayerCards(screen, len(game.players), blitDict, game, -1)