from board import Board
from boardMove import BoardMove
from move import Move
from space import Space
from teams import Team

class Game():
    
    def __init__(self):
        self.board = Board()
        self.turn = Team.WHITE
        self.must_double_jump_coordinate = None
    
    def move(self, move: Move):
        boardMove = BoardMove(move, self)
        (is_valid, message) = boardMove.handle_move()
        if not is_valid:
            raise ValueError(message)

    def get_space(self, row, col) -> Space:
        return self.board.get_space(row, col)

    def display(self):
        return self.board.display()

    def set_must_double_jump_next(self, row, col):
        self.must_double_jump_coordinate = (row, col)
    
    def change_turn(self):
        if self.turn == Team.WHITE:
            self.turn = Team.BLACK
        else:
            self.turn = Team.WHITE
    
    def get_possible_moves(self):
        return self.board.get_possible_moves(self) 

