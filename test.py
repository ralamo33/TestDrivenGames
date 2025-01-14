import unittest
from game import Game
from piece import Piece
from pieceDirection import PieceDirection
from space import Space
from teams import Team

class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    # Smaller step
    def test_get_starting_moves(self):
        moves = self.game.get_possible_moves()
        self.assertEqual(7, len(moves))
    
    def test_advanced_moves(self):
        self.game.move(2, 1, 3, 0)
        self.game.move(5, 0, 4, 1)
        self.game.move(2, 3, 3, 2)
        self.game.move(5, 2, 4, 3)
        self.game.move(1, 2, 2, 3)
        moves = self.game.get_possible_moves()
        self.assertEqual(8, len(moves))

    # def test_computer_player(self):
    #     game = Game()
    #     game.computer_move()

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_board_display(self):
        starting_display = '''_ W _ W _ W _ W
W _ W _ W _ W _
_ W _ W _ W _ W
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
B _ B _ B _ B _
_ B _ B _ B _ B
B _ B _ B _ B _'''
        self.assertEqual(starting_display, self.spaces.display())

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_down_valid(self):
        moving_piece = self.game.get_space(2, 1).piece
        self.game.move(row=2, col=1, toRow=3, toCol=0)
        piece_in_new_space = self.game.get_space(3, 0).piece
        self.assertEqual(moving_piece, piece_in_new_space)
        original_space = self.game.get_space(2, 1)
        self.assertIsNone(original_space.piece)
    
    def test_negative_row(self):
        with self.assertRaises(ValueError) as e:
            self.game.move(row=2, col=1, toRow=-1, toCol=0)
        self.assertEqual(str(e.exception), "Destination not on board")
    
    def test_negative_col(self):
        with self.assertRaises(ValueError) as e:
            self.game.move(row=2, col=1, toRow=3, toCol=-1)
        self.assertEqual(str(e.exception), "Destination not on board")
    
    
    def test_wrong_direction(self):
        self.game.move(row=2, col=1, toRow=3, toCol=0)
        with self.assertRaises(ValueError) as e:
            self.game.move(row=3, col=0, toRow=2, toCol=1)
        
        self.game.move(5, 0, 4, 1)
        with self.assertRaises(ValueError) as e:
            self.game.move(4, 1, 5, 0)
    
    def test_destination_over_board(self):
        with self.assertRaises(ValueError) as e:
            self.game.move(row=2, col=7, toRow=3, toCol=8)
        self.assertEqual(str(e.exception), "Destination not on board")

    def test_invalid_move_on_board(self):
        fromRow = 2
        fromCol = 1
        validMove1 = (3, 0)
        validMove2 = (3, 2)
        side_length = 8
        for toRow in range(side_length):
            for toCol in range(side_length):
                if toRow == 3 and toCol in [0, 2]:
                    continue
                with self.assertRaises(ValueError) as e:
                    self.game.move(fromRow, fromCol, toRow, toCol)
        
    def test_destination_has_another_piece(self):
        with self.assertRaises(ValueError) as e:
            self.game.move(0, 1, 1, 0)
        self.assertEqual(str(e.exception), "Destination has another piece")

    def test_eat_enemy(self):
        self.game.move(2, 1, 3, 0)
        self.game.move(5, 0, 4, 1)
        self.game.move(2, 3, 3, 2)
        self.game.move(5, 2, 4, 3)
        self.game.move(1, 2, 2, 3)
       
        orginal_piece = self.game.get_space(4, 3).piece
        self.game.move(4, 3, 2, 1)
        self.assertEqual(orginal_piece, self.game.get_space(2, 1).piece)
        self.assertIsNone(self.game.get_space(3, 2).piece)
        self.assertIsNone(self.game.get_space(4, 3).piece)
        self.game.move(2, 3, 3, 4)

    def test_cannot_eat_if_destination_filled(self):
        self.game.move(2, 1, 3, 0)
        self.game.move(5, 0, 4, 1)
        self.game.move(2, 3, 3, 2)
        self.game.move(5, 2, 4, 3)
        self.game.move(1, 0, 2, 1)
        self.game.move(5, 6, 4, 7)

        with self.assertRaises(ValueError) as e:
            self.game.move(3, 2, 5, 4)
        self.assertEqual(str(e.exception), "Destination has another piece")

    def test_cannot_eat_friend(self):
        self.game.move(2, 1, 3, 0)
        self.game.move(5, 0, 4, 1)
        self.game.move(2, 3, 3, 2)
        self.game.move(5, 2, 4, 3)
        self.game.move(1, 0, 2, 1)
        with self.assertRaises(ValueError) as e:
            self.game.move(6, 7, 4, 5)
        self.assertEqual(str(e.exception), "No enemy to jump over")

    def test_player_cannot_go_twice(self):
        self.game.move(2, 1, 3, 0)
        with self.assertRaises(ValueError) as e:
            self.game.move(3, 0, 4, 1)
        self.assertEqual(str(e.exception), "It is not your turn")
    
class DoubleJumpTests(unittest.TestCase):
    def setUp(self):
        self.board = Game()
        self.board.move(2, 1, 3, 0)
        self.board.move(5, 0, 4, 1)
        self.board.move(2, 3, 3, 2)
        self.board.move(5, 2, 4, 3)
        self.board.move(1, 2, 2, 3)
        self.board.move(4, 3, 2, 1)

    def test_double_jump(self):
        double_jump_piece = self.board.get_space(1, 0).piece
        self.board.move(1, 0, 3, 2)
        self.board.move(3, 2, 5, 0)
        self.assertEqual(double_jump_piece, self.board.get_space(5, 0).get_piece())
        self.assertTrue(self.board.get_space(2, 1).is_empty())
        self.assertTrue(self.board.get_space(4, 1).is_empty())
    
    def test_invalid_double_jump_move(self):
        self.board.move(1, 0, 3, 2)
        with self.assertRaises(ValueError) as e:
            self.board.move(3, 0, 5, 2)
        self.assertEqual(str(e.exception), "Must perform double jump.")
    

class TestSpace(unittest.TestCase):
    def setUp(self):
        self.white_piece = Piece(PieceDirection.DOWN, Team.WHITE)
        self.black_piece = Piece(PieceDirection.UP, Team.BLACK)

    def test_blank_space(self):
        space = Space()
        space_display = space.display()
        self.assertEqual("_", space_display)

    def test_white_space(self):
        space = Space()
        space.add_piece(self.white_piece)
        self.assertEqual("W", space.display())

    def test_black_space(self):
        space = Space()
        space.add_piece(self.black_piece)
        self.assertEqual("B", space.display())

    def test_is_empty(self):
        space = Space()
        self.assertTrue(space.is_empty())
        space.add_piece(self.white_piece)
        self.assertFalse(space.is_empty())




class TestPieceDirection(unittest.TestCase):
    def test_direction_is_valid(self):
        self.assertTrue(PieceDirection.UP.is_valid_direction(PieceDirection.UP))
        self.assertTrue(PieceDirection.DOWN.is_valid_direction(PieceDirection.DOWN))
        self.assertTrue(PieceDirection.BOTH.is_valid_direction(PieceDirection.UP))
        self.assertTrue(PieceDirection.BOTH.is_valid_direction(PieceDirection.DOWN))    

class TestPiece(unittest.TestCase):

    def setUp(self):
        self.piece = Piece(direction=PieceDirection.DOWN, team=Team.WHITE)
        self.upPiece = Piece(direction=PieceDirection.UP, team=Team.BLACK)
    
    def test_direction(self):
        self.assertTrue(self.piece.can_move_in_direction(PieceDirection.DOWN))
        self.assertFalse(self.piece.can_move_in_direction(PieceDirection.UP))

    def test_team(self):
        self.assertTrue(self.piece.on_team(Team.WHITE))
        self.assertFalse(self.piece.on_team(Team.BLACK))
    
    def test_against_team(self):
        self.assertTrue(self.piece.against_team(Team.BLACK))
        self.assertFalse(self.piece.against_team(Team.WHITE))

    def test_is_enemy(self):
        self.assertTrue(self.piece.is_enemy(self.upPiece))
        self.assertFalse(self.piece.is_enemy(self.piece))


if __name__ == "__main__":
    unittest.main()