import Constants
import Color

POSSIBLE_TWEAKS: dict[str, int] = {
    "ROTATE_LEFT": 0, "ROTATE_RIGHT": 1, "FLIP_HORIZONTAL": 2, "FLIP_VERTICAL": 3
}


class Piece:
    def __init__(self, grid: list[list[bool]], color: Color.Color) -> None:
        self.grid = grid
        self.color = color
        self._update_dimensions()

    def __str__(self) -> str:  # add color
        output = ""
        for line in self.grid:
            output += "".join(map(
                (lambda x: self.color.symbol if x else Constants.COLOR_PACK["BLACK"].symbol), line)) + "\n"
        return output

    def rotate(self, tweaks: list[int]):
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
        new_grid = [[False for _ in range(self.height)]
                    for __ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                new_grid[-1-j][i] = self.grid[i][j]
        self.grid = new_grid
        self._update_dimensions()
        return self

    def _rotate_right(self):
        new_grid = [[False for _ in range(self.height)]
                    for __ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                new_grid[j][-1-i] = self.grid[i][j]
        self.grid = new_grid
        self._update_dimensions()
        return self

    def _flip_horizontal(self):
        for line in self.grid:
            line.reverse()
            return self

    def _flip_vertical(self):
        self.grid.reverse()
        return self

    def _update_dimensions(self) -> None:
        self.height = len(self.grid)
        self.width = len(self.grid[0])
