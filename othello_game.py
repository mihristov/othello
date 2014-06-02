"""
TODO:
1. Is move valid and legal?
2. Find a square that forms a bracket with square for player in the given direction. Returns None if no such square exists.
3. Make move. Update the board to reflect the move by the specified player.
4. Flip pieces in the given direction as a result of the move by player.
5. Get a list of all legal moves for player and visualize them(optional).
6. Count points after every move.
"""
class Game:

    WHITE = 'W'
    BLACK = 'B'
    EMPTY = ' '
    WHITE_POINTS = 0
    BLACK_POINTS = 0

    EMPTY_BOARD = [EMPTY] * 64

    EMPTY_BOARD[27] = WHITE
    EMPTY_BOARD[28] = BLACK
    EMPTY_BOARD[35] = BLACK
    EMPTY_BOARD[36] = WHITE

    def __init__(self, board=None):
        self._board = board or self.EMPTY_BOARD[:]
        self._player = self.WHITE

    def outcome(self):
        mapping = {
            self.BLACK: 'B' ,
            self.WHITE: 'W',
            self.EMPTY: ' ',
        }
        return [mapping[s] for s in self.EMPTY_BOARD]

    def current_player(self):
        return self._player

    def play(self, position):
        if not self.valid_move(position):
            raise InvalidMoveError("Whoops!")
        self._board[position] = self._player

        if self._player == self.WHITE:
            self._player = self.BLACK
        else:
            self._player = self.WHITE

    def at(self, position):
        return self._board[position]

    def valid_move(self, position):
        return True

    def _player_on(self, indices):
        board = self._board
        squares = [board[i] for i in indices]

        if squares[0] == self.EMPTY:
            return None

        player = squares[0]

        if all(s == player for s in squares):
            return player
