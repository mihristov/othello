import random, copy
class Game:
    IN_PROGRESS = '<in-progress>'
    PLAYER_WINS = '<player-wins>'
    COMPUTER_WINS = '<computer-wins>'
    TIE = '<tie>'
    BOARDWIDTH = 8
    BOARDHEIGHT = 8
    EMPTYSPACE = 'E'
    WHITETILE = 'W'
    BLACKTILE = 'B'
    HINTTILE = 'H'

    def __init__(self, board = None):
        self.board = board or self.makeNewBoard()
        self.playerTile = self.WHITETILE
        self.computerTile = self.BLACKTILE

    def setPlayerWhite(self):
        self.playerTile = self.WHITETILE
        self.computerTile = self.BLACKTILE
        return [self.WHITETILE, self.BLACKTILE]

    def setPlayerBlack(self):
        self.playerTile = self.BLACKTILE
        self.computerTile = self.WHITETILE
        return [self.BLACKTILE, self.WHITETILE]

    def makeNewBoard(self):
        board = []
        for i in range(self.BOARDWIDTH):
            board.append([self.EMPTYSPACE] * self.BOARDHEIGHT)
        return board

    def resetBoard(self):
        for x in range(self.BOARDWIDTH):
            for y in range(self.BOARDHEIGHT):
                self.board[x][y] = self.EMPTYSPACE

        self.board[3][3] = self.WHITETILE
        self.board[3][4] = self.BLACKTILE
        self.board[4][3] = self.BLACKTILE
        self.board[4][4] = self.WHITETILE

    def getRandomPlayer(self):
        return random.choice(['computer', 'player']);

    def getAllValidMoves(self, board, tile):
        validMoves = []

        for x in range(self.BOARDWIDTH):
            for y in range(self.BOARDHEIGHT):
                if self.isMoveValid(board, tile, x, y) != False:
                    validMoves.append((x, y))
        return validMoves

    def isMoveValid(self, board, tile, xstart, ystart):
        if board[xstart][ystart] != self.EMPTYSPACE or not self.isInRangeOfBoard(xstart, ystart):
            return False

        board[xstart][ystart] = tile

        if tile == self.WHITETILE:
            otherTile = self.BLACKTILE
        else:
            otherTile = self.WHITETILE

        tilesToFlip = []
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x, y = xstart, ystart
            x += xdirection
            y += ydirection
            if self.isInRangeOfBoard(x, y) and board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not self.isInRangeOfBoard(x, y):
                    continue
                while board[x][y] == otherTile:
                    x += xdirection
                    y += ydirection
                    if not self.isInRangeOfBoard(x, y):
                        break
                if not self.isInRangeOfBoard(x, y):
                    continue
                if board[x][y] == tile:
                    while True:
                        x -= xdirection
                        y -= ydirection
                        if x == xstart and y == ystart:
                            break
                        tilesToFlip.append([x, y])

        board[xstart][ystart] = self.EMPTYSPACE
        if len(tilesToFlip) == 0:
            return False
        return tilesToFlip

    def isInRangeOfBoard(self, x, y):
        return x >= 0 and x < self.BOARDWIDTH and y >= 0 and y < self.BOARDHEIGHT

    def getAllValidMovesOfBoard(self, tile):
        dupeBoard = copy.deepcopy(self.board)

        for x, y in self.getAllValidMoves(dupeBoard, tile):
            dupeBoard[x][y] = self.HINTTILE
        return dupeBoard

    def makeMove(self, board, tile, xstart, ystart):
        tilesToFlip = self.isMoveValid(board, tile, xstart, ystart)

        if tilesToFlip == False:
            return False

        board[xstart][ystart] = tile

        for x, y in tilesToFlip:
            board[x][y] = tile
        return True

    def isOnCorner(self, x, y):
        return (x == 0 and y == 0) or \
               (x == self.BOARDWIDTH-1 and y == 0) or \
               (x == 0 and y == self.BOARDHEIGHT-1) or \
               (x == self.BOARDWIDTH-1 and y == self.BOARDHEIGHT-1)


    def getCompMoveCoords(self, computerTile):
        possibleMoves = self.getAllValidMoves(self.board, computerTile)

        random.shuffle(possibleMoves)

        for x, y in possibleMoves:
            if self.isOnCorner(x, y):
                return [x, y]

        bestScore = -1
        for x, y in possibleMoves:
            dupeBoard = copy.deepcopy(self.board)
            self.makeMove(dupeBoard, computerTile, x, y)
            score = self.getScore(dupeBoard)[computerTile]
            if score > bestScore:
                bestMove = [x, y]
                bestScore = score
        return bestMove

    def getScore(self, board):
        xscore = 0
        oscore = 0
        for x in range(self.BOARDWIDTH):
            for y in range(self.BOARDHEIGHT):
                if self.board[x][y] == self.WHITETILE:
                    xscore += 1
                if self.board[x][y] == self.BLACKTILE:
                    oscore += 1
        return {self.WHITETILE:xscore, self.BLACKTILE:oscore}

    def getOutcomeWithPoints(self):
        scores = self.getScore(self.board)

        if scores[self.playerTile] > scores[self.computerTile]:
            return 'You beat the computer by %s points! Congratulations!' % \
                   (scores[self.playerTile] - scores[self.computerTile])
        elif scores[self.playerTile] < scores[self.computerTile]:
            return 'You lost. The computer beat you by %s points.' % \
                   (scores[self.computerTile] - scores[self.playerTile])
        else:
            return 'The game was a tie!'

    def getOutcomeWithoutPoints(self):
        scores = self.getScore(self.board)

        for i in range(self.BOARDWIDTH):
            for j in range(self.BOARDHEIGHT):
                if self.board[i][j] == self.EMPTYSPACE:
                    return self.IN_PROGRESS

        if scores[self.playerTile] > scores[self.computerTile]:
            return self.PLAYER_WINS
        elif scores[self.playerTile] < scores[self.computerTile]:
            return self.COMPUTER_WINS
        else:
            return self.TIE
