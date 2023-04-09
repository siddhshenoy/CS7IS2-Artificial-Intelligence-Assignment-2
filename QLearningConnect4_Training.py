from Connect4.Connect4Board import Connect4
from Algorithms.QLearning import QLearningAgent
import pickle


Connect4Board = Connect4(dimensions=(4,4))

Connect4Board = QLearningAgent(0.6, 0.9, 0.4)
Connect4Board.Learn(Connect4Board, 700000)

pickle.dump(Connect4Board.GetQTable(), open("QTable_Connect4.pkl", "wb"))