# Artificial Intelligence - Assignment 2

## Libraries used:

1. python-tictactoe (https://pypi.org/project/python-tictactoe/)

## How to run the code:

There are two types of code files in this project. Four code files are for Human playing against AI. And two for training the QLearning agent for the respective boards.

`QLearningConnect4_Training.py` and `QLearningTicTacToe_Training.py` are the scripts for training the QLearning agent. For changing the board size in Connect4 kindly change the `dimensions` parameter in the constructor call for the `Connect4` board.

```
Connect4Board = Connect4(dimensions=(4,4))
                                     ^ ^
```

To play with the AI use the following four scripts:

`python AlphaBeta_Connect4.py`

`python AlphaBeta_TicTacToe.py`

`python QLearning_Connect4.py`

`python QLearning_TicTacToe.py`
