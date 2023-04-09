import math


class MiniMax:
    def __init__(self, player=-1) -> None:
        self.player = player
        self.total_states = 0
        
    def SetAIPlayer(self, player):
        self.player = player

    def GetMinimaxMove(self, board):
        self.total_states = 0
        bestScore = -math.inf
        bestMove = None
        copyboard = board.copy()
        for move in copyboard.possible_moves():
            self.total_states += 1
            tempCopy = copyboard.copy()
            copyboard.push(move)
            score = self.PerformMinimax(False, self.player, copyboard)
            copyboard = tempCopy.copy()
            if score > bestScore:
                bestScore = score
                bestMove = move
        return bestMove
    
    def PerformMinimax(self, isMaxTurn, maximizerMark, board):
        state = board.result()
        if state == 0:
            return 0
        elif (state == 1 or state == 2):
            return 100 if board.result() is maximizerMark else -100
        scores = []
        for move in board.possible_moves():
            self.total_states += 1
            _board = board.copy()
            _board.push(move)
            scores.append(self.PerformMinimax(not isMaxTurn, maximizerMark, _board))
        return max(scores) if isMaxTurn else min(scores)

    def GetTotalStates(self):
        return self.total_states