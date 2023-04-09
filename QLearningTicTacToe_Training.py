from tictactoe import Board
from Algorithms.QLearning import QLearningAgent
from tictactoe import Board
import pickle


TicTacToeBoard = Board(dimensions=(3,3))
TicTacToeAgent = QLearningAgent(0.3, 0.9, 0.9)
TicTacToeAgent.Learn(TicTacToeBoard, 500)
pickle.dump(TicTacToeAgent.GetQTable(), open("QTable_TicTacToe.pkl", "wb"))