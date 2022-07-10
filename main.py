import Player
import Piece
import Board
import Constants
import colorit
import random
from UserException import UserException


colorit.init_colorit()

board: Board.Board = Board.Board([
    Player.Player(name="Sa", color=Constants.COLOR_PACK["RED"]),
    Player.Player(name="Sy", color=Constants.COLOR_PACK["YELLOW"]),
    Player.Player(name="Mo", color=Constants.COLOR_PACK["GREEN"]),
    Player.Player(name="Ma", color=Constants.COLOR_PACK["BLUE"])
])

# print(board)
# player_index = 0
# def call_for_input(board: Board.Board) -> tuple[int]:
#     inp = input(f"Action ({board.players[player_index].name}):\n")
#     try:
#         piece_index, x_left, y_top = map(lambda x: int(x), inp.split("/"))
#     except Exception as e:
#         print(e)
#         piece_index = random.randint(0, len(player.pieces) - 1)
#         x_left = random.randint(0, board.width - 1)
#         y_top = random.randint(0, board.height - 1)
#     return (piece_index, x_left, y_top)


# while True:
#     player = board.players[player_index]
#     piece_index, x_left, y_top = call_for_input(board)
#     piece = player.pieces[piece_index]

#     try:
#         board.put(player_index, piece_index, x_left, y_top)
#         player_index = (player_index+1) % 4
#         print(board)
#     except UserException as e:
#         print("-------IMPOSSIBLE-------")
#         print(e)
#         print(piece)
#         print("x = " + str(x_left) + " | y = " + str(y_top))
#         print("------------------------")

print(board)
