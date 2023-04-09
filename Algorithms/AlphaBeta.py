from tictactoe import Board

import math

class AlphaBeta:
    def __init__(self) -> None:
        self.AIPlayer = None
        self.total_states = 0
    def SetAIPlayer(self, player):
        self.AIPLayer = player
    
    def GetTotalStates(self):
        return self.total_states
    
    def ResetTotalStates(self):
        self.total_states = 0

    def GetNextMove(self, board, max_player_playing, alpha, beta):
        PlayerWon = board.result()
        if PlayerWon == 0:
            return 0, None
        elif PlayerWon == 2:
            return -10, None
        elif PlayerWon == 1:
            return 10, None
            
        if max_player_playing:
            bv = -math.inf
            choice = None
            for move in board.possible_moves():
                self.total_states += 1
                _board = board.copy()
                _board.push(move)
                val, moveab = self.GetNextMove(_board, False, alpha, beta)
                if val > bv:
                    bv = val
                    choice = move
                alpha = max(alpha, bv)
                if beta <= alpha:
                    break
            return bv, choice
        else:
            bv = math.inf
            choice = None
            for move in board.possible_moves():
                self.total_states += 1
                _board = board.copy()
                _board.push(move)
                val, moveab = self.GetNextMove(_board, True, alpha, beta)
                if val < bv:
                    bv = val
                    choice = move
                beta = min(beta, bv)
                if beta <= alpha:
                    break
            return bv, choice