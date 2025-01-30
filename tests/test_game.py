import unittest
from tic_tac_toe_game.game import TicTacToe
import numpy as np

class TestTicTacToe(unittest.TestCase):
    def test_reset(self):
        # Initialize the game with a custom board and player
        game = TicTacToe(starting_player=2, board=np.array([[1, 2, 0], [0, 1, 2], [2, 1, 0]]))
        
        # Call the reset method
        game.reset()
        
        # Check if the board is reset to a 3x3 matrix of zeros
        np.testing.assert_array_equal(game.board, np.zeros((3, 3)))
        
        # Check if the current player is set to 1
        self.assertEqual(game.current_player, 1)

    def test_get_valid_moves(self):
        #Create game with custom board
        game = TicTacToe(starting_player=1, board=np.array([[1, 2, 0], [0, 1, 2], [2, 1, 0]]))
        valid_moves = game.get_valid_moves()
        expected_moves = np.array([[0, 2], [1, 0], [2, 2]])
        np.testing.assert_array_equal(valid_moves, expected_moves)

    def test_make_move(self):
        #Create game with custom board
        game = TicTacToe(starting_player=1)
        game.make_move(0, 0)
        self.assertEqual(game.board[0, 0], 1)
        self.assertEqual(game.current_player, 2)

    def test_invalid_move(self):
        #Create game with custom board with a move already made at 0,0
        game = TicTacToe(starting_player=1, board=np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
        with self.assertRaises(ValueError):
            game.make_move(0, 0)

    def test_check_winner(self):
        #Create game with custom board with winning state
        game = TicTacToe(starting_player=1, board=np.array([[1, 1, 1], [0, 2, 0], [0, 0, 2]]))
        winner = game.check_winner()
        self.assertEqual(winner, 1)

    def test_is_game_over(self):
        #Create game with custom board with winning state
        game = TicTacToe(starting_player=1, board=np.array([[1, 1, 1], [0, 2, 0], [0, 0, 2]]))
        self.assertTrue(game.is_game_over())

    def test_print_board(self):
        #Create game with custom board
        game = TicTacToe(starting_player=1, board=np.array([[1, 2, 0], [0, 1, 2], [2, 1, 0]]))
        game.print_board()
        # TODO: need to add assert here that checks the printed output

    def test_step(self):
        #Create game with custom board
        game = TicTacToe(starting_player=1)
        game.step((0, 0))
        self.assertEqual(game.board[0, 0], 1)
        self.assertEqual(game.current_player, 2)


if __name__ == '__main__':
    unittest.main()