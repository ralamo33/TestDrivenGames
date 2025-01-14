from boardMove import BoardMove
from coordinate import Coordinate
from piece import Piece
from pieceDirection import PieceDirection
from space import Space
from teams import Team


class Board():
    def __init__(self):
        self.board: list[list[Space]] = []
        for _ in range(8):
            row = []
            for _ in range(8):
                row.append(Space())
            self.board.append(row)
        self._add_starting_pieces()
    
    def get_space_from_coordinate(self, coordinate: Coordinate) -> Space:
        row_len = len(self.board)
        col_len = len(self.board[0])
        row = coordinate.row
        col = coordinate.col
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

    def get_possible_moves(self, game):
        moves = [] 
        for r_idx, row in enumerate(self.board):
            for c_idx, space in enumerate(row):
                if space.is_empty():
                    continue
                piece = space.get_piece()
                if not piece.on_team(game.turn):
                    continue
                moves_to_check = self.get_moves_to_check(r_idx, c_idx)
                for move in moves_to_check:
                    (r, c) = move
                    boardMove = BoardMove(r_idx, c_idx, r, c, game)
                    is_valid_with_explanation = boardMove.is_valid_with_explanation()
                    if is_valid_with_explanation[0]:
                        moves.append((r, c))
        return moves

    
    def get_moves_to_check(self, row: int, col: int):
        standard_moves = [
            (row + 1, col + 1),
            (row + 1, col + -1),
            (row + -1, col + 1),
            (row + -1, col + -1)
        ]
        jump_moves = [
            (row + 2, col + 2),
            (row + 2, col + -2),
            (row + -2, col + 2),
            (row + -2, col + -2)
        ]
        return standard_moves + jump_moves

    def _add_starting_pieces(self):
        white_board = [
            self.get_space_from_coordinate(Coordinate(0, 1)),
            self.get_space_from_coordinate(Coordinate(0, 3)),
            self.get_space_from_coordinate(Coordinate(0, 5)),
            self.get_space_from_coordinate(Coordinate(0, 7)),
            self.get_space_from_coordinate(Coordinate(1, 0)),
            self.get_space_from_coordinate(Coordinate(1, 2)),
            self.get_space_from_coordinate(Coordinate(1, 4)),
            self.get_space_from_coordinate(Coordinate(1, 6)),
            self.get_space_from_coordinate(Coordinate(2, 1)),
            self.get_space_from_coordinate(Coordinate(2, 3)),
            self.get_space_from_coordinate(Coordinate(2, 5)),
            self.get_space_from_coordinate(Coordinate(2, 7)),
        ]
        black_board = [
            self.get_space_from_coordinate(Coordinate(5, 0)),
            self.get_space_from_coordinate(Coordinate(5, 2)),
            self.get_space_from_coordinate(Coordinate(5, 4)),
            self.get_space_from_coordinate(Coordinate(5, 6)),
            self.get_space_from_coordinate(Coordinate(6, 1)),
            self.get_space_from_coordinate(Coordinate(6, 3)),
            self.get_space_from_coordinate(Coordinate(6, 5)),
            self.get_space_from_coordinate(Coordinate(6, 7)),
            self.get_space_from_coordinate(Coordinate(7, 0)),
            self.get_space_from_coordinate(Coordinate(7, 2)),
            self.get_space_from_coordinate(Coordinate(7, 4)),
            self.get_space_from_coordinate(Coordinate(7, 6)),
        ]
        for space in white_board:
            space.add_piece(Piece(PieceDirection.DOWN, Team.WHITE))
        
        for space in black_board:
            space.add_piece(Piece(PieceDirection.UP, Team.BLACK))
