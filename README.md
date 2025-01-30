

![Coverage](https://raw.githubusercontent.com/andrewbeaton123/tic_tac_toe_game/main/coverage.svg)
# TicTacToe Game

`tic_tac_toe_game` is a Python package that implements a simple, functional Tic-Tac-Toe game. It is designed to be used with reinforecement learning code, making moves, checking the winner, and handling board state. The package is designed to be easy to use and integrate into other projects, and it supports a variety of game operations such as resetting the game, making moves, checking for a winner, and printing the board.

## Features

- **Game Initialization**: Start a game with a specified starting player.
- **Board Representation**: The board is represented as a 3x3 NumPy array.
- **Valid Moves**: Get a list of valid moves on the current board.
- **Move Execution**: Make moves for player 1 (`X`) and player 2 (`O`).
- **Winner Check**: Check for the winner or if the game ended in a draw.
- **Reset**: Reset the board and start a new game.
- **Terminal Display**: Print the board state in a readable format in the terminal.
- **Game Over Check**: Determine if the game has ended.

## Installation

To install the package, you can use `pip`:

```bash
pip install tic_tac_toe_game
```

##  Usage 
```python
from tic_tac_toe_game import TicTacToe

game = TicTacToe(starting_player=1)

game.make_move(0, 0)  # Player 1 makes a move at row 0, column 0
game.make_move(1, 1)  # Player 2 makes a move at row 1, column 1

winner = game.check_winner()  # Returns 1, 2 for winner or 0 for a draw

game.print_board()

game.reset()
```

MIT License
