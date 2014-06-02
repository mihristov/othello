import unittest

from othello_game import Game


class GameTest(unittest.TestCase):

    def CreateTable(self, board):
        possibilities = {
            'B': Game.BLACK,
            'W': Game.WHITE,
            ' ': Game.EMPTY
        }
        state = [possibilities[s] for s in board]
        return Game(state)

    def assertOutcome(self, expected_outcome, board):
        game = self.CreateTable(board)

        self.assertEqual(
            game.outcome(),
            expected_outcome)

    def testDeterminingIfNewGame(self):
        self.assertOutcome(Game.EMPTY_BOARD, [
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', 'W', 'B', ' ', ' ', ' ',
            ' ', ' ', ' ', 'B', 'W', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ])

if __name__ == '__main__':
    unittest.main()
