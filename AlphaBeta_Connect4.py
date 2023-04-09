from Connect4.Connect4Board import Connect4
from Algorithms.AlphaBeta import *
from Algorithms.Agent import *

AIPlayer = None
HumanPlayer = None

PlayerTurn = input("Which player do you want to play?\n")
HumanPlayer = int(PlayerTurn)

if HumanPlayer == 1:
    AIPlayer = 2
else:
    AIPlayer = 1

AlphaBetaAgent = AlphaBeta()
AlphaBetaAgent.SetAIPlayer(AIPlayer)

connect4_x = int(input("Enter the width of the board\n"))
connect4_y = int(input("Enter the width of the board\n"))

GameBoard = Connect4(dimensions=(connect4_x,connect4_y))

Maximizing = False
if AIPlayer == 1:
    Maximizing = True
else:
    Maximizing = False

while GameBoard.result() == None:
    if GameBoard.turn == AIPlayer:
        print("AI is thinking..")
        Val, Move = AlphaBetaAgent.GetNextMove(GameBoard, Maximizing, -math.inf, math.inf)
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

