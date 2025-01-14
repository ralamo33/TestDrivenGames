from piece import Piece
from pieceDirection import PieceDirection
from space import Space
from teams import Team


class Board():
    def __init__(self):
        self.board = []
        for _ in range(8):
            row = []
            for _ in range(8):
                row.append(Space())
            self.board.append(row)
        self._add_starting_pieces()

    def get_space(self, row, col) -> Space:
        row_len = len(self.board)
        col_len = len(self.board[0])
        if row >= 0 and col >= 0 and row < row_len and col < col_len:
            return self.board[row][col]
        return None

    def display(self):
        display_str = ""
        for row in self.board:
            for space in row:
                display_str += space.display()
                display_str += " "
            display_str = display_str[:-1]
            display_str += "\n"
        display_str = display_str[:-1]
        return display_str


    def _add_starting_pieces(self):
        white_board = [
            self.get_space(0, 1),
            self.get_space(0, 3),
            self.get_space(0, 5),
            self.get_space(0, 7),

            self.get_space(1, 0),
            self.get_space(1, 2),
            self.get_space(1, 4),
            self.get_space(1, 6),

            self.get_space(2, 1),
            self.get_space(2, 3),
            self.get_space(2, 5),
            self.get_space(2, 7),
        ]
        black_board = [
            self.get_space(5, 0),
            self.get_space(5, 2),
            self.get_space(5, 4),
            self.get_space(5, 6),

            self.get_space(6, 1),
            self.get_space(6, 3),
            self.get_space(6, 5),
            self.get_space(6, 7),

            self.get_space(7, 0),
            self.get_space(7, 2),
            self.get_space(7, 4),
            self.get_space(7, 6),
        ]
        for space in white_board:
            space.add_piece(Piece(PieceDirection.DOWN, Team.WHITE))
        
        for space in black_board:
            space.add_piece(Piece(PieceDirection.UP, Team.BLACK))
