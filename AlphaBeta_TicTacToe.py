from tictactoe import Board
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

GameBoard = Board(dimensions=(3,3))

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
        X = int(input("Enter X Coordinate\n"))
        Y = int(input("Enter Y Coordinate\n"))
        GameBoard.push((X, Y))
    print(GameBoard)

if GameBoard.result() == AIPlayer:
    print("AI won!")
elif GameBoard.result() == HumanPlayer:
    print("Human won!")
elif GameBoard.result() == 0:
    print("Game was a draw")
