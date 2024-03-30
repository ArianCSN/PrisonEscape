from Map01 import map01
from Map02 import map02
from GameOver import game_over
from Menu import main_menu

# define the initial player position for map 01
x_pos = 390
y_pos = 435

# define the map number
flag = "main_menu"

# turn on and off developer mode (map pos and player and bots hit box and more...)
developer_mode = 0

while True:

    if flag == "main_menu":
        flag, developer_mode = main_menu()

    if flag == "map01":
        flag, x_pos, y_pos = map01(x_pos, y_pos, developer_mode)

    if flag == "map02":
        flag, x_pos, y_pos = map02(x_pos, y_pos, developer_mode)

    if flag == "game_over":
        flag = game_over()
