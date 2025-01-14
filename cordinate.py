class Coordinate:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
    
    def __eq__(self, value):
        return self.row == value.row and self.col == value.col