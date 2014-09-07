import unittest

from othello_game import Game

class GameTest(unittest.TestCase):
    def createGame(self, board):
        mapping = {
            'W': Game.WHITETILE,
            'B': Game.BLACKTILE,
            'E': Game.EMPTYSPACE,
        }
        newBoard = []
        for i in range(len(board)):
            newBoard.append([mapping[s] for s in board[i]])
        return Game(newBoard)

    def assertOutcome(self, expected_outcome, board):
        game = self.createGame(board)

        self.assertEqual(
                game.getOutcomeWithoutPoints(),
                expected_outcome)

    def testDeterminingInProgress(self):
        self.assertOutcome(Game.IN_PROGRESS, [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'E', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
        ])

        self.assertOutcome(Game.IN_PROGRESS, [
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
        ])

    def testDeterminingWinPlayer(self): #suppose player is white by default
        self.assertOutcome(Game.PLAYER_WINS, [
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ])
        self.assertOutcome(Game.PLAYER_WINS, [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ])
        self.assertOutcome(Game.PLAYER_WINS, [
            ['B', 'W', 'B', 'W', 'W', 'W', 'B', 'B'],
            ['B', 'W', 'W', 'B', 'B', 'W', 'W', 'B'],
            ['W', 'W', 'B', 'B', 'W', 'W', 'B', 'W'],
            ['W', 'B', 'B', 'W', 'W', 'B', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['W', 'W', 'B', 'B', 'W', 'W', 'B', 'B'],
            ['W', 'W', 'B', 'W', 'W', 'W', 'W', 'B'],
            ['W', 'B', 'W', 'W', 'B', 'W', 'W', 'B']
        ])

    def testDeterminingWinComputer(self): #suppose player is white by default
        self.assertOutcome(Game.COMPUTER_WINS, [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
        ])
        self.assertOutcome(Game.COMPUTER_WINS, [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ])
        self.assertOutcome(Game.COMPUTER_WINS, [
            ['B', 'W', 'B', 'W', 'W', 'W', 'B', 'B'],
            ['B', 'W', 'W', 'B', 'B', 'W', 'W', 'B'],
            ['W', 'W', 'B', 'B', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'B', 'W', 'W', 'B', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'W', 'B'],
            ['W', 'B', 'W', 'W', 'B', 'B', 'W', 'B']
        ])

    def testDeterminingTie(self): #suppose player is white by default
        self.assertOutcome(Game.TIE, [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ])

    def testPlayingAMove(self):
        game = Game()
        game.resetBoard()

        self.assertEqual(game.getOutcomeWithoutPoints(),
                Game.IN_PROGRESS)

        self.assertTrue(game.isMoveValid(game.board, game.computerTile, 5, 4))

        game.makeMove(game.board, game.computerTile, 4, 5)

        self.assertFalse(game.isMoveValid(game.board, game.computerTile, 5, 4))

    def testMovesOutsideTheBoardAreInvalid(self):
        game = Game()
        game.resetBoard()
        self.assertFalse(game.isMoveValid(game.board, game.computerTile, -1, 4))
        self.assertFalse(game.isMoveValid(game.board, game.computerTile, 5, -1))

    def testMoveOnOccupiedSquareIsInvalid(self):
        game = self.createGame([
            ['B', 'E', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ])

        self.assertTrue(game.isMoveValid(game.board, game.playerTile, 0, 1))
        self.assertFalse(game.isMoveValid(game.board, game.computerTile, 1, 4))

    def testMakeMoveOnCorner(self):
        game = self.createGame([
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'W', 'W', 'E'],
            ['E', 'E', 'E', 'E', 'W', 'B', 'W', 'E'],
            ['E', 'E', 'E', 'E', 'W', 'W', 'W', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
            ])

        expectedMove = [0, 7]
        self.assertEqual(game.getCompMoveCoords(game.computerTile), expectedMove)

if __name__ == '__main__':
    unittest.main()
