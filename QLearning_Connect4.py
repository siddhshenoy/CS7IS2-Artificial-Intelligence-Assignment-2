from Connect4.Connect4Board import Connect4
from Algorithms.AlphaBeta import *
from Algorithms.Agent import *
from Algorithms.QLearning import QLearningAgent
from Algorithms.Agent import Agent
import pickle
AIPlayer = None
HumanPlayer = None

pickle_files = [
    "./Models/QLearning_Connect4_4x4_0.2_0.6_0.7.pkl",
    "./Models/QLearning_Connect4_4x4_0.6_0.9_0.4.pkl"
]

PlayerTurn = input("Which player do you want to play?\n")
HumanPlayer = int(PlayerTurn)

print("\n")
for i in range(len(pickle_files)):
    print("{} : {}".format(i, pickle_files[i]))

PickleFileId = input("Which pickle file do you want to choose?\n")

if HumanPlayer == 1:
    AIPlayer = 2
else:
    AIPlayer = 1

TicTacToeAgent = QLearningAgent(alpha=0.0, gamma=0.0, epsilon=0.0)
qFile = open(pickle_files[int(PickleFileId)], "rb")
q_table = dict()
q_table = pickle.load(qFile)
TicTacToeAgent.SetQTable(q_table)

GameBoard = Connect4(dimensions=(4,4))

Maximizing = False
if AIPlayer == 1:
    Maximizing = True
else:
    Maximizing = False

while GameBoard.result() == None:
    if GameBoard.turn == AIPlayer:
        print("AI is thinking..")
        Move = TicTacToeAgent.GetMoveParameters(GameBoard)
        GameBoard.push(Move)
    elif GameBoard.turn == HumanPlayer:
        col = int(input("Enter column\n"))
        GameBoard.push(col)
    print(GameBoard)

if GameBoard.result() == AIPlayer:
    print("AI won!")
elif GameBoard.result() == HumanPlayer:
    print("Human won!")
elif GameBoard.result() == 0:
    print("Game was a draw")

