import Piece
import Color
import colorit


COLOR_PACK: dict[str, Color.Color] = {
    "BLACK": Color.Color((56, 56, 56), "⬛"),
    "BLUE": Color.Color(colorit.Colors.blue, "🟦"),
    "BROWN": Color.Color((142, 86, 46), "🟫"),
    "GREEN": Color.Color(colorit.Colors.green, "🟩"),
    "RED": Color.Color(colorit.Colors.red, "🟥"),
    "YELLOW": Color.Color(colorit.Colors.yellow, "🟨"),
    "WHITE": Color.Color(colorit.Colors.white, "⬜"),
    "ORANGE": Color.Color(colorit.Colors.orange, "🟧"),
    "PURPLE": Color.Color(colorit.Colors.purple, "🟪"),
}


def get_initial_pieces(color: Color.Color):
    return[
        # 1
        Piece.Piece([[True]], color),
        # 2
        Piece.Piece([[True], [True]], color),
        # 3
        Piece.Piece([[True], [True], [True]], color),
        Piece.Piece([[True, True], [True, False]], color),
        # 4
        Piece.Piece([[True, True, True, True]], color),
        Piece.Piece([[True, True, True], [True, False, False]], color),
        Piece.Piece([[True, True, False], [False, True, True]], color),
        Piece.Piece([[False, True, False], [True, True, True]], color),
        Piece.Piece([[True, True], [True, True]], color),
        # 5
        Piece.Piece([[True, True, True, True, True]], color),  # 5*1
        Piece.Piece([[True, False, False, False], [
            True, True, True, True]], color),  # 4*2
        Piece.Piece([[True, True, False, False], [
                    False, True, True, True]], color),
        Piece.Piece([[False, True, False, False], [
                    True, True, True, True]], color),
        Piece.Piece([[True, True], [True, True], [True, False]], color),  # 3*2
        Piece.Piece([[True, True], [True, False], [True, True]], color),
        Piece.Piece([[True, False, False], [True, False, False],
                    [True, True, True]], color),  # 3*3
        Piece.Piece([[True, False, False], [True, True, False],
                     [False, True, True]], color),
        Piece.Piece([[True, True, False], [False, True, False],
                     [False, True, True]], color),
        Piece.Piece([[False, True, False], [True, True, True],
                     [False, True, False]], color),
        Piece.Piece([[True, False, False], [True, True, True],
                     [False, True, False]], color),
        Piece.Piece([[False, True, False], [False, True, False],
                    [True, True, True]], color)
    ]
