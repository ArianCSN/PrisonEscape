from Map00 import map00
from Map01 import map01
from GameOver import show_game_over

# define the initial player position for map 00
x_pos = 390
y_pos = 435

# define the map number
flag = "00"

# turn on and off developer mode (map pos and player and bots hit box)
developer_mode = 1

while True:
    if flag == "00":
        flag, x_pos, y_pos = map00(x_pos, y_pos, developer_mode)

    # if flag == "01":
    #     flag, x_pos, y_pos = map01(x_pos, y_pos, developer_mode)

    if flag == "game_over":
        show_game_over()
        flag = "00"
