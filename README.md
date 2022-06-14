# Blokus
Implementation of the Blokus board game in Python

### Rules:
https://www.ultraboardgames.com/blokus/game-rules.php

### Usage
How to setup a game:
```py
import Constants
from Board import Board
from Player import Player

board = Board([
    Player(name="P1", color=Constants.COLOR_PACK["RED"]),
    Player(name="P2", color=Constants.COLOR_PACK["YELLOW"]),
    Player(name="P3", color=Constants.COLOR_PACK["GREEN"]),
    Player(name="P4", color=Constants.COLOR_PACK["BLUE"])
])

print(board)

player_index = 0
piece_index = 11
print(board.players[player_index].pieces[piece_index])

board.put(player_index, piece_index, 10, 10)
print(board)
```