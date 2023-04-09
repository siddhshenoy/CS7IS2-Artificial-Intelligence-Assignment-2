from tictactoe import Board
import numpy as np
import random

class Agent:
    @staticmethod
    def GetRandomPlayerMove(board):
        if board.__class__.__name__ == "Board":
            return tuple(random.choice(board.possible_moves()).tolist())
        else:
            return random.choice(board.possible_moves())


    @staticmethod
    def GetDefaultPlayerMove(board, player, opponent):

        for move in board.possible_moves():
            _board = board.copy()
            if _board.__class__.__name__ == "Board":
                _board.set_mark(tuple(move.tolist()), opponent)
            elif _board.__class__.__name__ == "Connect4":
                _board.set_markc4(move, opponent)
            if _board.result() == player:
                return move
            
        #Block if the player did not win in the next move
        for move in board.possible_moves():
            _board = board.copy()
            if _board.__class__.__name__ == "Board":
                _board.set_mark(tuple(move.tolist()), opponent)
            elif _board.__class__.__name__ == "Connect4":
                _board.set_markc4(move, opponent)
            if _board.result() == opponent:
                return move
            
        return random.choice(board.possible_moves())


                