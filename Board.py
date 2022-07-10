import Constants
import Player
import Piece
from UserException import UserException

PLAYER_STARTING_CORNER = [(0, 0), (-1, 0), (-1, -1), (0, -1)]


class Board:
    def __init__(self, players: list[Player.Player], width: int = 20, height: int = 20) -> None:
        self.width = width
        self.height = height
        self.grid = [[-1 for _ in range(width)] for __ in range(height)]
        self.players = players
        self.num_of_players = len(players)
        self.players_played_turns = [0 for _ in range(self.num_of_players)]

    def __str__(self) -> str:
        output = "┌"+"─"*self.width*2+"┐\n"
        for line in self.grid:
            output += "│"
            for element in line:
                if (element == -1):
                    output += Constants.COLOR_PACK["BLACK"].symbol
                else:
                    output += self.players[element].color.symbol
            output += "│\n"
        return output+"└"+"─"*self.width*2+"┘"

    def __repr__(self) -> str:
        return self.__str__()

    def put(self, player_index: int, piece_index: int, x_left: int, y_top: int) -> None:
        player = self.players[player_index]
        piece = player.pieces[piece_index]

        # region: Error handling
        if (player._has_used_piece(piece_index)):
            raise UserException("The piece is already used")

        elif (self._check_if_outside(piece, x_left, y_top)):
            raise UserException("The piece is outside of the board")

        elif (self.players_played_turns[player_index] == 0):
            if (not self._check_starting_position(player_index, piece, x_left, y_top)):
                raise UserException(
                    "The piece is not connected to the corner of the board")

        elif (self._check_if_collides(piece, x_left, y_top)):
            raise UserException("The piece collides with another piece")

        elif (self._check_if_borders_touch(player_index, piece, x_left, y_top)):
            raise UserException(
                "The piece touches another piece of the same color")

        elif (not self._check_if_corners_connected(player_index, piece, x_left, y_top)):
            raise UserException(
                "The piece is not connected to any piece of the same color")

        for (i, line) in enumerate(piece.grid):
            for (j, exists) in enumerate(line):
                if exists:
                    self.grid[y_top+i][x_left+j] = player_index

        try:
            player._use_piece(piece_index)
        except UserException as e:
            self.remove(player_index, piece_index, x_left, y_top)
            raise e
        self.players_played_turns[player_index] += 1

    def _check_if_outside(self, piece: Piece.Piece, x_left: int, y_top: int) -> bool:
        return not ((0 <= x_left <= self.width-piece.width) and (0 <= y_top <= self.height-piece.height))

    def _check_if_collides(self, piece: Piece.Piece, x_left: int, y_top: int) -> bool:
        for (i, line) in enumerate(piece.grid):
            for (j, exists) in enumerate(line):
                global_x = x_left+j
                global_y = y_top+i
                if (exists) and (self.grid[global_y][global_x] != -1):
                    return True
        return False

    def _check_if_borders_touch(self, player_index: int, piece: Piece.Piece, x_left: int, y_top: int) -> bool:
        for border in piece.borders:
            border_x, border_y = border.split(";")
            global_x = int(border_x)+x_left
            global_y = int(border_y)+y_top
            if (self._coords_are_inside_grid(global_x, global_y)) and (self.grid[global_y][global_x] == player_index):
                return True
        return False

    def _check_if_corners_connected(self, player_index: int, piece: Piece.Piece, x_left: int, y_top: int) -> bool:
        for corner in piece.corners:
            corner_x, corner_y = corner.split(";")
            global_x = int(corner_x)+x_left
            global_y = int(corner_y)+y_top
            if (self._coords_are_inside_grid(global_x, global_y)) and (self.grid[int(corner_y)+y_top][int(corner_x)+x_left] == player_index):
                return True
        return False

    def _check_starting_position(self, player_index, piece: Piece.Piece, x_left: int, y_top: int) -> bool:
        starting_corner = PLAYER_STARTING_CORNER[player_index]

        if not piece.grid[starting_corner[1]][starting_corner[0]]:
            return False

        return all([(piece.width + x_left == self.width) if starting_corner[0] == -1 else (x_left == 0),
                    (piece.height + y_top == self.height) if starting_corner[1] == -1 else (y_top == 0)])

    def _coords_are_inside_grid(self, x, y) -> bool:
        return (0 <= x < self.width and 0 <= y < self.height)
