import numpy as np

class TicTacToe:
    def __init__(self,starting_player:int, board =None):
        
        self.current_player = starting_player # Player 1 starts
        self.winner =0 # currently a draw 
        if board is None:
            self.board = np.zeros((3, 3))  # 3x3 Tic Tac Toe board
        else :
            self.board = board
            
    def __str__(self):
        """
        Returns a string representation of the TicTacToe game.

        The string includes the current player, the winner, and the current state of the board.

        Returns:
            str: A formatted string representing the current state of the game.
        """
        return f"TicTacToe(current_player={self.current_player}, winner={self.winner}, board=\n{self.board})"

    def reset(self):
        """
        Resets the game board to its initial state and sets the current player to player 1.

        This method initializes the game board to a 3x3 matrix of zeros, representing an empty board,
        and sets the current player to 1, indicating that player 1 will make the next move.
        """
        self.board = np.zeros((3, 3))
        self.current_player = 1

    def get_valid_moves(self):
        """
        Get a list of valid moves on the current game board.

        Returns:
            numpy.ndarray: An array of coordinates where the board is empty (value is 0).
        """
        return np.argwhere(self.board == 0)

    def make_move(self, row, col):
        """
        Makes a move on the Tic-Tac-Toe board.

        Args:
            row (int): The row index where the move is to be made (0-indexed).
            col (int): The column index where the move is to be made (0-indexed).

        Raises:
            ValueError: If the move is invalid (i.e., the cell is already occupied).

        Side Effects:
            Updates the board with the current player's move.
            Checks for a winner after the move.
            Switches the current player.
        """
        if self.board[row, col] == 0:
            self.board[row, col] = self.current_player
            self.check_winner()
            self.current_player = 3 - self.current_player  # Switch players (1 -> 2, 2 -> 1)
        else:
            raise ValueError("Invalid move")

    def check_winner(self):
        """
        Checks the current state of the board to determine if there is a winner.

        Returns:
            int: The player number (1 or 2) if there is a winner.
            0: If the game is a draw (no valid moves left).
            None: If the game is still ongoing and there is no winner yet.
        """
        for player in [1, 2]:
            # Check rows, columns, and diagonals for a win
            if np.any(np.all(self.board == player, axis=0)) or \
               np.any(np.all(self.board == player, axis=1)) or \
               np.all(np.diag(self.board) == player) or \
               np.all(np.diag(np.fliplr(self.board)) == player):
                self.winner = player
                return player
        if len(self.get_valid_moves()) == 0:
            return 0  # Draw
        return None  # Game is ongoing

    def is_game_over(self):
        """
        Check if the game is over.

        Returns:
            bool: True if there is a winner, False otherwise.
        """
        return self.check_winner() is not None

    def print_board(self):
        """
        Prints the current state of the tic-tac-toe board.

        The board is represented as a 2D list where:
        - 1 represents a cell occupied by player 'X'
        - 2 represents a cell occupied by player 'O'
        - 0 represents an empty cell

        The board is printed with 'X' for player 1, 'O' for player 2, and spaces for empty cells.
        Each row of the board is separated by a line of dashes.
        """
        for row in self.board:
            print(" | ".join(["X" if cell == 1 else "O" if cell == 2 else " " for cell in row]))
            print("-" * 9)

    def step(self, action):
        """
        Executes a move in the game if the game is not over and the action is valid.

        Parameters:
        action (tuple): A tuple containing the row and column indices for the move.

        Returns:
        int: The winner of the game if the game is over and there is a winner (1 for player 1).
        """
        if not self.is_game_over() and action in self.get_valid_moves():
            row, col = action
            self.make_move(row, col)
            if self.is_game_over():
                if self.winner == 1:
                    return self.winner