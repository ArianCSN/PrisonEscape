from Map01 import map01
from GameOver import game_over
from Menu import main_menu

# define the initial player position for map 00
x_pos = 390
y_pos = 435

# define the map number
flag = "main_menu"

# turn on and off developer mode (map pos and player and bots hit box)
developer_mode = 0

while True:

    if flag == "main_menu":
        flag, developer_mode = main_menu()

    if flag == "01":
        flag, x_pos, y_pos = map01(x_pos, y_pos, developer_mode)

    # if flag == "01":
    #     flag, x_pos, y_pos = map01(x_pos, y_pos, developer_mode)

    if flag == "game_over":
        flag = game_over()
