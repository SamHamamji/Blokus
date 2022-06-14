import Constants
import Color

POSSIBLE_TWEAKS: dict[str, int] = {
    "ROTATE_LEFT": 0, "ROTATE_RIGHT": 1, "FLIP_HORIZONTAL": 2, "FLIP_VERTICAL": 3
}


class Piece:
    def __init__(self,
                 grid: list[list[bool]],
                 color: Color.Color,
                 tiles: set[str] = None,
                 corners: set[str] = None,
                 borders: set[str] = None
                 ) -> None:
        self.grid = grid
        self.color = color
        self._update_dimensions()
        if (tiles == None or corners == None or borders == None):
            self._generate_square_groups()

    def __str__(self) -> str:  # add color
        output = ""
        for line in self.grid:
            output += "".join(map(
                (lambda x: self.color.symbol if x else Constants.COLOR_PACK["BLACK"].symbol), line)) + "\n"
        return output

    def square_groups_representation(self):
        output = ""
        for y in range(-1, self.height+1):
            for x in range(-1, self.width+1):
                if (self._is_inside_grid(x, y) and self.grid[y][x]):
                    output += Constants.COLOR_PACK["WHITE"].symbol
                elif (str(x)+";"+str(y) in self.borders):
                    output += Constants.COLOR_PACK["RED"].symbol
                elif (str(x)+";"+str(y) in self.corners):
                    output += Constants.COLOR_PACK["GREEN"].symbol
                else:
                    output += Constants.COLOR_PACK["BLACK"].symbol
            output += "\n"
        return output[:-1]

    def tweak(self, tweaks: list[int]):
        for tweak in tweaks:
            if (tweak == POSSIBLE_TWEAKS.ROTATE_LEFT):
                self._rotateLeft()
            elif (tweak == POSSIBLE_TWEAKS.ROTATE_RIGHT):
                self._rotate_right()
            elif (tweak == POSSIBLE_TWEAKS.FLIP_HORIZONTAL):
                self._flip_horizontal()
            elif (tweak == POSSIBLE_TWEAKS.FLIP_VERTICAL):
                self._flip_vertical()
        return self

    def _rotate_left(self):

        def _rotate_square_left(s: str) -> str:
            coord = s.split(";")
            return coord[1]+";"+str(self.height - 1 - int(coord[0]))

        new_grid = [[False for _ in range(self.height)]
                    for __ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                new_grid[-1-j][i] = self.grid[i][j]
        self.grid = new_grid
        self._update_dimensions()
        self.tiles = set(map(_rotate_square_left, self.tiles))
        self.borders = set(map(_rotate_square_left, self.borders))
        self.corners = set(map(_rotate_square_left, self.corners))
        return self

    def _rotate_right(self):
        def _rotate_square_right(s: str) -> str:
            coord = s.split(";")
            return str(self.width - 1 - int(coord[1]))+";" + coord[0]

        new_grid = [[False for _ in range(self.height)]
                    for __ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                new_grid[j][-1-i] = self.grid[i][j]
        self.grid = new_grid
        self._update_dimensions()

        self.tiles = set(map(_rotate_square_right, self.tiles))
        self.borders = set(map(_rotate_square_right, self.borders))
        self.corners = set(map(_rotate_square_right, self.corners))
        return self

    def _flip_horizontal(self):

        def _flip_square_horizontal(s: str) -> str:
            i = s.index(";")
            return str(self.height - 1 - int(s[:i])) + s[i:]

        for line in self.grid:
            line.reverse()

        self.tiles = set(map(_flip_square_horizontal, self.tiles))
        self.borders = set(map(_flip_square_horizontal, self.borders))
        self.corners = set(map(_flip_square_horizontal, self.corners))

        return self

    def _flip_vertical(self):
        def _flip_square_vertical(s: str) -> str:
            i = s.index(";") + 1
            return s[:i]+str(self.width - 1 - int(s[i:]))

        self.grid.reverse()

        self.tiles = set(map(_flip_square_vertical, self.tiles))
        self.borders = set(map(_flip_square_vertical, self.borders))
        self.corners = set(map(_flip_square_vertical, self.corners))

        return self

    def _update_dimensions(self) -> None:
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def _generate_square_groups(self) -> None:
        self.tiles: set[str] = set()
        self.borders: set[str] = set()
        self.corners: set[str] = set()
        for y in range(-1, self.height+1):
            for x in range(-1, self.width+1):
                # check if tile
                if ((self._is_inside_grid(x, y)) and self.grid[y][x]):
                    self.tiles.add(f"{x};{y}")
                # check if border
                else:
                    isBorder = False
                    for diffx, diffy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if (self._is_inside_grid(x+diffx, y+diffy) and self.grid[y+diffy][x+diffx]):
                            self.borders.add(f"{x};{y}")
                            isBorder = True
                            break
                    # check if corner
                    if(not isBorder):
                        for diffx, diffy in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
                            if (self._is_inside_grid(x+diffx, y+diffy) and self.grid[y+diffy][x+diffx]):
                                self.corners.add(f"{x};{y}")
                                break

    def _is_inside_grid(self, x, y) -> bool:
        return (0 <= x < self.width and 0 <= y < self.height)


def get_initial_pieces(color: Color.Color):
    return[
        # 1
        Piece([[True]], color),
        # 2
        Piece([[True], [True]], color),
        # 3
        Piece([[True], [True], [True]], color),
        Piece([[True, True], [True, False]], color),
        # 4
        Piece([[True, True, True, True]], color),
        Piece([[True, True, True], [True, False, False]], color),
        Piece([[True, True, False], [False, True, True]], color),
        Piece([[False, True, False], [True, True, True]], color),
        Piece([[True, True], [True, True]], color),
        # 5
        Piece([[True, True, True, True, True]], color),  # 5*1
        Piece([[True, False, False, False], [
            True, True, True, True]], color),  # 4*2
        Piece([[True, True, False, False], [
            False, True, True, True]], color),
        Piece([[False, True, False, False], [
            True, True, True, True]], color),
        Piece([[True, True], [True, True], [True, False]], color),  # 3*2
        Piece([[True, True], [True, False], [True, True]], color),
        Piece([[True, False, False], [True, False, False],
               [True, True, True]], color),  # 3*3
        Piece([[True, False, False], [True, True, False],
               [False, True, True]], color),
        Piece([[True, True, False], [False, True, False],
               [False, True, True]], color),
        Piece([[False, True, False], [True, True, True],
               [False, True, False]], color),
        Piece([[True, False, False], [True, True, True],
               [False, True, False]], color),
        Piece([[False, True, False], [False, True, False],
               [True, True, True]], color)
    ]


# red = Constants.COLOR_PACK["RED"]
# initial_pieces = get_initial_pieces(red)
