"""
    This code is just an extension of the normal python-tictactoe board and changes a few functions
    in order to make it work like Connect4.
"""

from tictactoe import Board
import numpy as np
import numpy.typing as npt
from typing import List, Tuple, Iterable, Optional, Union

class Connect4(Board):
    def __init__(self, dimensions: Iterable[int] = ...) -> None:
        super().__init__(dimensions, x_in_a_row=4)
        self.state_dict = dict()

    def possible_moves(self) -> npt.NDArray[np.int64]:
        # print("X In a row: {}".format(self.x_in_a_row))
        possible_moves_list = []
        for move in super().possible_moves():
            if move[0] in possible_moves_list:
                continue
            else:
                possible_moves_list.append(move[0])
        return possible_moves_list

    def push(self, col):
        for move in super().possible_moves():
            self.state_dict[move[0]] = []
        for move in super().possible_moves():
            self.state_dict[move[0]].append(move[1])
        # print(self.state_dict)
        # print("Next Push: {} {}".format(col, max(self.state_dict[col])))
        super().push((col, max(self.state_dict[col])))
        # print(self)

    def copy(self):
        """
        Get a copy of the board.
        :return: A copy of the board.
        """
        board = Connect4(self.dimensions)
        board.turn = self.turn
        board.board = self.board.copy()
        return board
    def set_markc4(self, col, player: int) -> None:
        for move in super().possible_moves():
            self.state_dict[move[0]] = []
        for move in super().possible_moves():
            self.state_dict[move[0]].append(move[1])
        super().set_mark((col, max(self.state_dict[col])), player)
