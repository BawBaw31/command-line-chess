
from typing import Tuple
from .Piece import Piece


class Bishop(Piece):
    def __init__(self, coor: Tuple[str, int], color: str):
        super().__init__(coor, color)

    def move(self, coor: Tuple[str, int]):
        if abs(ord(self.coor[0]) - ord(coor[0])) == abs(self.coor[1] - coor[1]):
            self.coor = coor
            return True
        return False

    def render(self):
        if self.color == "white":
            return "♗"
        else:
            return "♝"
