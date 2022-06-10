import Player
import Piece
import Board
import Constants
import colorit
import random


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

while True:
    playerIndex = random.randint(0, board.num_of_players - 1)
    player = board.players[playerIndex]
    pieceIndex = random.randint(0, len(player.pieces) - 1)
    piece = player.pieces[pieceIndex]
    x = random.randint(0, board.width - 1)
    y = random.randint(0, board.height - 1)
    if(board._check_if_inside(piece, x, y)):
        board.put(playerIndex, pieceIndex, x, y)
        print(board)
    else:
        print("-------IMPOSSIBLE-------")
        print(piece)
        print("x = " + str(x) + " | y = " + str(y))
    input("")

print(board)
