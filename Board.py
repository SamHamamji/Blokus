import Constants
import Player
import Piece


class Board:
    def __init__(self, players: list[Player.Player], width: int = 20, height: int = 20) -> None:
        self.width = width
        self.height = height
        self.grid = [[-1 for _ in range(width)] for __ in range(height)]
        self.players = players
        self.num_of_players = len(players)

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

    def put(self, playerIndex: int, PieceIndex: int, x_left: int, y_top: int) -> None:
        piece = self.players[playerIndex].pieces[PieceIndex]
        if (self._check_if_inside(piece, x_left, y_top)):
            raise Exception("The piece is outside of the board")
        # Check initial corner
        # Check inside board
        # Check collisions
        # Check piece corners
        # put the numbers (player indexes) in the grid
        for (i, line) in enumerate(piece.grid):
            for(j, exists) in enumerate(line):
                if exists:
                    self.grid[y_top+i][x_left+j] = playerIndex
        pass

    def _check_if_inside(self, Piece: Piece.Piece, x_left: int, y_top: int) -> bool:
        return (0 <= x_left <= self.width-Piece.width) and (0 <= y_top <= self.height-Piece.height)