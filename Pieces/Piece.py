from typing import Tuple


class Piece:
    # (x, y) coordinate of the piece
    coor: Tuple[str, int]
    # The color of the piece
    color: str

    # constructor
    def __init__(self, coor: Tuple[str, int], color: str):
        self.coor = coor
        self.color = color
