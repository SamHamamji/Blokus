import Player
import Piece
import Board
import Constants
import colorit
import random
from UserException import UserException


colorit.init_colorit()

Sam = Player.Player(name="Sam", color=Constants.COLOR_PACK["RED"])
Sylva = Player.Player(name="Sylva", color=Constants.COLOR_PACK["YELLOW"])
Monique = Player.Player(name="Monique", color=Constants.COLOR_PACK["GREEN"])
Marc = Player.Player(name="Marc", color=Constants.COLOR_PACK["BLUE"])

board = Board.Board([
    Player.Player(name="Sam", color=Constants.COLOR_PACK["RED"]),
    Player.Player(name="Sylva", color=Constants.COLOR_PACK["YELLOW"]),
    Player.Player(name="Monique", color=Constants.COLOR_PACK["GREEN"]),
    Player.Player(name="Marc", color=Constants.COLOR_PACK["BLUE"])
])

print(board)

playerIndex = -1
while True:
    playerIndex = (playerIndex+1) % 4
    player = board.players[playerIndex]
    pieceIndex = random.randint(0, len(player.pieces) - 1)
    piece = player.pieces[pieceIndex]
    x = random.randint(0, board.width - 1)
    y = random.randint(0, board.height - 1)

    try:
        board.put(playerIndex, pieceIndex, x, y)
        print(board)
    except UserException as e:
        print("-------IMPOSSIBLE-------")
        print(e)
        print(piece)
        print("x = " + str(x) + " | y = " + str(y))
        print("------------------------")
    # except Exception as e:
    #     print("-------IMPOSSIBLE-------")
    #     print(e)
    #     print(piece)
    #     print("x = " + str(x) + " | y = " + str(y))
    #     print("------------------------")
    #     break

    input("")

print(board)
