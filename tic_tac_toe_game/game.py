import numpy as np

class TicTacToe:
    def __init__(self, starting_player: int = 1, board=None):
        """
        Initializes the TicTacToe game.

        Args:
            starting_player (int): The player who starts the game (1 or 2).
            board (np.ndarray, optional): A 3x3 array to initialize the board state.
        """
        self.starting_player = starting_player
        self.current_player = starting_player
        self.winner = None  # None: ongoing, 0: draw, 1 or 2: winner
        
        if board is None:
            self.board = np.zeros((3, 3), dtype=int)
        else:
            self.board = np.array(board, dtype=int)
            
    def __str__(self):
        """
        Returns a string representation of the TicTacToe game.
        """
        return f"TicTacToe(current_player={self.current_player}, winner={self.winner}, board=\n{self.board})"

    def reset(self):
        """
        Resets the game to its initial state using the original starting player.
        """
        self.current_player = self.starting_player
        self.winner = None
        self.board = np.zeros((3, 3), dtype=int)

    def get_valid_moves(self):
        """
        Get a list of valid moves on the current game board.

        Returns:
            list: A list of (row, col) tuples where the board is empty.
        """
        return [tuple(move) for move in np.argwhere(self.board == 0)]

    def make_move(self, row, col):
        """
        Makes a move on the Tic-Tac-Toe board.

        Args:
            row (int): The row index (0-indexed).
            col (int): The column index (0-indexed).

        Raises:
            ValueError: If the move is invalid or the game is already over.
        """
        if self.winner is not None:
            raise ValueError("Game is already over")
        if self.board[row, col] != 0:
            raise ValueError("Invalid move: Cell already occupied")
            
        self.board[row, col] = self.current_player
        self.check_winner()
        
        if self.winner is None:
            self.current_player = 3 - self.current_player
        return self.winner

    def check_winner(self):
        """
        Checks the current state of the board to determine if there is a winner or draw.

        Returns:
            int or None: 1 or 2 for a winner, 0 for a draw, None if ongoing.
        """
        for player in [1, 2]:
            if np.any(np.all(self.board == player, axis=0)) or \
               np.any(np.all(self.board == player, axis=1)) or \
               np.all(np.diag(self.board) == player) or \
               np.all(np.diag(np.fliplr(self.board)) == player):
                self.winner = player
                return player
        
        if len(self.get_valid_moves()) == 0:
            self.winner = 0  # Draw
            return 0
            
        return None

    def is_game_over(self):
        """
        Check if the game is over.

        Returns:
            bool: True if there is a winner or a draw, False otherwise.
        """
        return self.check_winner() is not None

    def print_board(self):
        """
        Prints the current state of the board.
        """
        for row in self.board:
            print(" | ".join(["X" if cell == 1 else "O" if cell == 2 else " " for cell in row]))
            print("-" * 9)

    def step(self, action):
        """
        Executes a move and returns the new state, winner, and done flag.
        
        Args:
            action: Either a (row, col) tuple or an integer index into valid moves.
        """
        if isinstance(action, (int, np.integer)):
            moves = self.get_valid_moves()
            if action < len(moves):
                row, col = moves[action]
            else:
                raise ValueError("Action index out of range")
        else:
            row, col = action
            
        self.make_move(row, col)
        return self.board, self.winner, self.is_game_over()
