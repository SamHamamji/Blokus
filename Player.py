import Color
import Piece
from UserException import UserException


class Player:
    def __init__(self, color: Color.Color, name: str = "Unknown", pieces: list[Piece.Piece] = None) -> None:
        self.name = name
        self.color = color
        self.pieces = pieces if (
            pieces != None) else Piece.get_initial_pieces(color)
        self.used_pieces = []

    def _has_used_piece(self, piece_index: int) -> bool:
        return self.pieces[piece_index] == None

    def _use_piece(self, piece_index: int) -> None:
        # region: Error handling
        if (piece_index < 0 or piece_index >= len(self.pieces)):
            raise UserException("The piece index is out of range")
        elif (self._has_used_piece(piece_index)):
            raise UserException("The piece is already used")

        self.used_pieces.append(self.pieces[piece_index])
        self.pieces[piece_index] = None
