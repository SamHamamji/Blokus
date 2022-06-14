import Color
import Constants
import Piece


class Player:
    def __init__(self, color: Color.Color, name: str = "Unknown", pieces: list[Piece.Piece] = None) -> None:
        self.name = name
        self.color = color
        self.pieces = pieces if (
            pieces != None) else Piece.get_initial_pieces(color)
