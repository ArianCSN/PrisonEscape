from Map00 import map00
from GameOver import show_game_over


flag = 00

while True:
    if flag == 00:
        flag = map00()

    if flag == "game_over":
        show_game_over()
        flag = 00
