import sys, pygame, time
from pygame.locals import *
from othello_game import *

game = Game()


class Gui():
    WIN_WIDTH = 640
    WIN_HEIGHT = 480
    SPACEPIXELS = 50
    FPS = 10
    XBOARD = int((WIN_WIDTH - (game.BOARDWIDTH * SPACEPIXELS)) / 2)
    YBOARD = int((WIN_HEIGHT - (game.BOARDHEIGHT * SPACEPIXELS)) / 2)

    WHITE      = (255, 255, 255)
    BLACK      = (0, 0, 0)
    GREEN      = (0, 155, 0)
    BROWN      = (174, 94, 0)

    def __init__(self):
        pygame.init()
        self.isDualPlayers = False
        self.CLOCK = pygame.time.Clock()
        self.DISPLAYBG = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        pygame.display.set_caption('Othello')
        self.FONT = pygame.font.Font('freesansbold.ttf', 16)
        self.BIGFONT = pygame.font.Font('freesansbold.ttf', 32)

        DISPLAYBOARD = pygame.image.load('othello_board.jpg')
        DISPLAYBOARD = pygame.transform.smoothscale(DISPLAYBOARD, (game.BOARDWIDTH * self.SPACEPIXELS, game.BOARDHEIGHT * self.SPACEPIXELS))
        DISPLAYBOARDRECT = DISPLAYBOARD.get_rect()
        DISPLAYBOARDRECT.topleft = (self.XBOARD, self.YBOARD)
        self.getCompMoveCoords = pygame.image.load('othello_bg.jpg')
        self.getCompMoveCoords = pygame.transform.smoothscale(self.getCompMoveCoords, (self.WIN_WIDTH, self.WIN_HEIGHT))
        self.getCompMoveCoords.blit(DISPLAYBOARD, DISPLAYBOARDRECT)

        while True:
            if self.runGame() == False:
                break

    def runGame(self):
        game.resetBoard()
        turn = game.getRandomPlayer()

        self.drawBoard(game.board)
        playerTile, pcTile = self.enterPlayerTile()

        ngSurf = self.FONT.render('New Game', True, self.WHITE)
        ngRect = ngSurf.get_rect()
        ngRect.topleft = (10 , 10)

        # text2Surf = self.BIGFONT.render('Do you want to play vs computer or player?', True, self.WHITE, self.GREEN)
        # text2Rect = text2Surf.get_rect()
        # text2Rect.center = (int(self.WIN_WIDTH / 2), int(self.WIN_HEIGHT / 2))

        # playerSurf = self.BIGFONT.render('Player', True, self.WHITE, self.GREEN)
        # playerRect = playerSurf.get_rect()
        # playerRect.center = (int(self.WIN_WIDTH / 2) - 60, int(self.WIN_HEIGHT / 2) + 90)

        # pcSurf = self.BIGFONT.render('Computer', True, self.WHITE, self.GREEN)
        # pcRect = pcSurf.get_rect()
        # pcRect.center = (int(self.WIN_WIDTH / 2) + 60, int(self.WIN_HEIGHT / 2) + 90)

        # while True:
        #     self.checkForQuit()
        #     for event in pygame.event.get():
        #         if event.type == MOUSEBUTTONUP:
        #             mousex, mousey = event.pos
        #             if playerRect.collidepoint( (mousex, mousey) ):
        #                 self.isDualPlayers = True
        #                 break
        #             elif pcRect.collidepoint( (mousex, mousey) ):
        #                 self.isDualPlayers = False
        #                 break
        #     self.DISPLAYBG.blit(text2Surf, text2Rect)
        #     self.DISPLAYBG.blit(playerSurf, playerRect)
        #     self.DISPLAYBG.blit(pcSurf, pcRect)
        #     pygame.display.update()
        #     self.CLOCK.tick(self.FPS)

        while True:
            if turn == 'player':
                if game.getAllValidMoves(game.board, playerTile) == []:
                    break
                movexy = None
                while movexy == None:
                    boardToDraw = game.getAllValidMovesOfBoard(playerTile)

                    self.checkForQuit()
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONUP:
                            mousex, mousey = event.pos
                            if ngRect.collidepoint( (mousex, mousey) ):
                                return True
                            movexy = self.getCoordsClicked(mousex, mousey)
                            if movexy != None and not game.isMoveValid(game.board, playerTile, movexy[0], movexy[1]):
                                movexy = None

                    self.drawBoard(boardToDraw)
                    self.drawScore(boardToDraw, playerTile, pcTile, turn)

                    self.DISPLAYBG.blit(ngSurf, ngRect)

                    self.CLOCK.tick(self.FPS)
                    pygame.display.update()

                game.makeMove(game.board, playerTile, movexy[0], movexy[1])

                if game.getAllValidMoves(game.board, pcTile) != []:
                    turn = 'computer'

            else:
                if game.getAllValidMoves(game.board, pcTile) == []:
                    break
                x, y = None, None
                if self.isDualPlayers:
                    movexy = None
                    while movexy == None:
                        boardToDraw = game.getAllValidMovesOfBoard(pcTile)

                        self.checkForQuit()
                        for event in pygame.event.get():
                            if event.type == MOUSEBUTTONUP:
                                mousex, mousey = event.pos
                                if ngRect.collidepoint( (mousex, mousey) ):
                                    return True
                                movexy = self.getCoordsClicked(mousex, mousey)
                                if movexy != None and not game.isMoveValid(game.board, pcTile, movexy[0], movexy[1]):
                                    movexy = None

                        self.drawBoard(boardToDraw)
                        self.drawScore(boardToDraw, playerTile, pcTile, turn)

                        self.DISPLAYBG.blit(ngSurf, ngRect)
                        self.CLOCK.tick(self.FPS)
                        pygame.display.update()
                    x = movexy[0]
                    y = movexy[1]
                else:
                    pauseUntil = time.time() + random.randint(5, 15) * 0.1
                    while time.time() < pauseUntil:
                        pygame.display.update()

                    x, y = game.getCompMoveCoords(pcTile)
                game.makeMove(game.board, pcTile, x, y)
                if game.getAllValidMoves(game.board, playerTile) != []:
                    turn = 'player'

        self.drawBoard(game.board)

        text = game.getOutcomeWithPoints()
        textSurf = self.FONT.render(text, True, self.WHITE, self.GREEN)
        textRect = textSurf.get_rect()
        textRect.center = (int(self.WIN_WIDTH / 2), int(self.WIN_HEIGHT / 2))
        self.DISPLAYBG.blit(textSurf, textRect)

        text2Surf = self.BIGFONT.render('Play again?', True, self.WHITE, self.GREEN)
        text2Rect = text2Surf.get_rect()
        text2Rect.center = (int(self.WIN_WIDTH / 2), int(self.WIN_HEIGHT / 2) + 50)

        yesSurf = self.BIGFONT.render('Yes', True, self.WHITE, self.GREEN)
        yesRect = yesSurf.get_rect()
        yesRect.center = (int(self.WIN_WIDTH / 2) - 60, int(self.WIN_HEIGHT / 2) + 90)

        noSurf = self.BIGFONT.render('No', True, self.WHITE, self.GREEN)
        noRect = noSurf.get_rect()
        noRect.center = (int(self.WIN_WIDTH / 2) + 60, int(self.WIN_HEIGHT / 2) + 90)

        while True:
            self.checkForQuit()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if yesRect.collidepoint( (mousex, mousey) ):
                        return True
                    elif noRect.collidepoint( (mousex, mousey) ):
                        return False
            self.DISPLAYBG.blit(textSurf, textRect)
            self.DISPLAYBG.blit(text2Surf, text2Rect)
            self.DISPLAYBG.blit(yesSurf, yesRect)
            self.DISPLAYBG.blit(noSurf, noRect)
            pygame.display.update()
            self.CLOCK.tick(self.FPS)

    def drawBoard(self, board):
        self.DISPLAYBG.blit(self.getCompMoveCoords, self.getCompMoveCoords.get_rect())

        for x in range(game.BOARDWIDTH + 1):
            startx = (x * self.SPACEPIXELS) + self.XBOARD
            starty = self.YBOARD
            endx = (x * self.SPACEPIXELS) + self.XBOARD
            endy = self.YBOARD + (game.BOARDHEIGHT * self.SPACEPIXELS)
            pygame.draw.line(self.DISPLAYBG, self.BLACK, (startx, starty), (endx, endy))
        for y in range(game.BOARDHEIGHT + 1):
            startx = self.XBOARD
            starty = (y * self.SPACEPIXELS) + self.YBOARD
            endx = self.XBOARD + (game.BOARDWIDTH * self.SPACEPIXELS)
            endy = (y * self.SPACEPIXELS) + self.YBOARD
            pygame.draw.line(self.DISPLAYBG, self.BLACK, (startx, starty), (endx, endy))

        for x in range(game.BOARDWIDTH):
            for y in range(game.BOARDHEIGHT):
                centerx, centery = self.translateBoardToPixelCoord(x, y)
                if board[x][y] == game.WHITETILE or board[x][y] == game.BLACKTILE:
                    if board[x][y] == game.WHITETILE:
                        tileColor = self.WHITE
                    else:
                        tileColor = self.BLACK
                    pygame.draw.circle(self.DISPLAYBG, tileColor, (centerx, centery), int(self.SPACEPIXELS / 2) - 4)
                if board[x][y] == game.HINTTILE:
                    pygame.draw.rect(self.DISPLAYBG, self.BROWN, (centerx - 4, centery - 4, 8, 8))

    def translateBoardToPixelCoord(self, x, y):
        return self.XBOARD + x * self.SPACEPIXELS + int(self.SPACEPIXELS / 2), self.YBOARD + y * self.SPACEPIXELS + int(self.SPACEPIXELS / 2)

    def enterPlayerTile(self):

        textSurf = self.FONT.render('Do you want to be white or black?', True, self.WHITE, self.GREEN)
        textRect = textSurf.get_rect()
        textRect.center = (int(self.WIN_WIDTH / 2), int(self.WIN_HEIGHT / 2))

        xSurf = self.BIGFONT.render('White', True, self.WHITE, self.GREEN)
        xRect = xSurf.get_rect()
        xRect.center = (int(self.WIN_WIDTH / 2) - 60, int(self.WIN_HEIGHT / 2) + 40)

        oSurf = self.BIGFONT.render('Black', True, self.BLACK, self.GREEN)
        oRect = oSurf.get_rect()
        oRect.center = (int(self.WIN_WIDTH / 2) + 60, int(self.WIN_HEIGHT / 2) + 40)

        while True:
            self.checkForQuit()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if xRect.collidepoint( (mousex, mousey) ):
                        return game.setPlayerWhite()
                    elif oRect.collidepoint( (mousex, mousey) ):
                        return game.setPlayerBlack()

            self.DISPLAYBG.blit(textSurf, textRect)
            self.DISPLAYBG.blit(xSurf, xRect)
            self.DISPLAYBG.blit(oSurf, oRect)
            pygame.display.update()
            self.CLOCK.tick(self.FPS)


    def checkForQuit(self):
        for event in pygame.event.get((QUIT, KEYUP)): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    def drawScore(self, board, playerTile, pcTile, turn):
        score = game.getScore(board)
        scoreSurf = self.FONT.render("Player : %s    Computer : %s    %s's Turn" % (str(score[playerTile]), str(score[pcTile]), turn.title()), True, self.WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.bottomleft = (10, self.WIN_HEIGHT - 5)
        self.DISPLAYBG.blit(scoreSurf, scoreRect)

    def getCoordsClicked(self, mousex, mousey):
        for x in range(game.BOARDWIDTH):
            for y in range(game.BOARDHEIGHT):
                if mousex > x * self.SPACEPIXELS + self.XBOARD and \
                   mousex < (x + 1) * self.SPACEPIXELS + self.XBOARD and \
                   mousey > y * self.SPACEPIXELS + self.YBOARD and \
                   mousey < (y + 1) * self.SPACEPIXELS + self.YBOARD:
                    return (x, y)
        return None

if __name__ == '__main__':
    Gui()
