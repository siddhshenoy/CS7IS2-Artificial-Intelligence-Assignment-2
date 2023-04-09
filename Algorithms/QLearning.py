from Connect4.Connect4Board import Connect4
import numpy as np
import random

class QLearningAgent:
    def __init__(self, alpha, gamma, epsilon) -> None:
        self.QTable = dict()
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        print("Initializing QLearning algorithm (alpha = {}, gamma = {}, epsilon = {})".format(self.alpha, self.gamma, self.epsilon))
    
        
    def GetReward(self, board):
        if board.result() is not None:
            if board.result() == 1:
                return 2
            elif board.result() == 2:
                return -2
            elif board.result() == 0:
                return 0.5
        else:
            return 0

    def RandomMove(self, board):
        choice = []
        for moves in board.possible_moves():
            if board.__class__.__name__ == "Board":
                choice.append((moves[0], moves[1]))
            else:
                choice.append(moves)
        return random.choice(choice)

    def PlayerWinMove(self, board, chance):
        for move in board.possible_moves():
            _board = board.copy()
            _board.push(move)
            if _board.result() == chance:
                return move
        return None

    def OpponentMove(self, board, chance):
        if chance == 2:
            opponent = 1
        else:
            opponent = 2
        for move in board.possible_moves():
            _board = board.copy()
            if board.__class__.__name__ == "Board":
                _board.set_mark(tuple(move.tolist()), opponent)
            else:
                _board.set_markc4(move.tolist(), opponent)
            if _board.result() == opponent:
                return move
        return None

    def MakeDefaultPlayerMove(self, board, chance):
        _move = self.PlayerWinMove(board, chance)
        if _move is not None:
            if board.__class__.__name__ == "Board":
                return tuple(_move.tolist())
            else:
                return _move
        
        _move = self.OpponentMove(board, chance)
        #print("Block Move: {}".format(blockMove))
        if _move is not None:
            if board.__class__.__name__ == "Board":
                return tuple(_move.tolist())
            else:
                return _move
        return self.RandomMove(board)

    def BoardKey(self, board):
        return str([str(i) for i in board.board.flatten().tolist()])

    def CreateStateEntry(self,board):
        default_val = 1
        key = (str(self.BoardKey(board)), board.turn)
        if self.QTable.get(key) is None:
            moves = board.possible_moves()
            if board.__class__.__name__ == "Board":
                self.QTable[key] = {
                    tuple(move.tolist()): default_val for move in moves
                }
            else:
                self.QTable[key] = {
                    move: default_val for move in moves
                }
        return key

    def MinMaxVal(self, q_values, minmax):
        mmq = minmax(list(q_values.values()))
        q_vals = list(q_values.values())
        count = q_vals.count(minmax)
        if count > 1:
            nMoves = [move for move in list(q_values.keys()) if q_values[move] == mmq]
            rIdx = np.random.choice(len(nMoves))
            move = nMoves[rIdx]
        else:
            move = minmax(q_values, key=q_values.get)
        return move

    def GetMoveParameters(self, board):
        if np.random.uniform() < self.epsilon:
            return self.MakeDefaultPlayerMove(board, board.turn)
        else:
            state_key = self.CreateStateEntry(board)
            q_value = self.QTable[state_key]
            if board.turn == 1:
                return self.MinMaxVal(q_value, max)
            elif board.turn == 2:
                return self.MinMaxVal(q_value, min)

    def PerformOperation(self, board, move):
        sk = self.CreateStateEntry(board)
        _board = board.copy()
        _board.push(move)
        reward = self.GetReward(_board)
        nsk = self.CreateStateEntry(_board)
        if _board.result() is not None:
            expected = reward
        else:
            nextQ = self.QTable[nsk]
            if _board.turn == 1:
                #expected = reward + (self.gamma * min(nextQ.values()))
                expected = min(nextQ.values())
            elif _board.turn == 2:
                #expected = reward + (self.gamma * max(nextQ.values()))
                expected = max(nextQ.values())
            self.QTable[sk][move] += self.alpha * (reward + (self.gamma * expected) - self.QTable[sk][move])
            

    def Learn(self, board, episodes):
        # print("1")
        for i in range(episodes):
            if i % 500 == 0:
                print("Rounds {}".format(i))
            _board = board.copy()
            while _board.result() is None:
                if _board.turn == 1:
                    move1 = self.GetMoveParameters(_board)
                    self.PerformOperation(_board, move1)
                    _board.push(move1)
                elif _board.turn == 2:
                    move2 = self.GetMoveParameters(_board)
                    self.PerformOperation(_board, move2)
                    _board.push(move2)

    def GetQTable(self):
        return self.QTable


    def SetQTable(self, qtable):
        self.QTable = qtable