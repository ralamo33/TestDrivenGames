from piece import Piece
from teams import Team


class Space:
    def __init__(self):
        self.piece = None

    def add_piece(self, piece):
        self.piece = piece

    def delete_piece(self):
        self.piece = None
    
    def get_piece(self) -> Piece:
        if self.piece is None:
            raise ValueError("Piece does not exist")
        return self.piece
    
    def is_empty(self):
        return self.piece is None
    
    def display(self):
        if self.piece is None:
            return "_"
        return self.piece.team[0]