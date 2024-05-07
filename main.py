from GameOver import game_over
from Menu import main_menu
from Map01 import map01
from Map02 import map02
from Map03 import map03
from Map04 import map04


# define the initial player position for map01
x_pos = 780
y_pos = 390

# define the map number
flag = "main_menu"

# Developer Mode Flag
# - Set to 1 to enable developer-specific features (e.g., display map positions, hit boxes).
# - When enabled, additional information useful for debugging or development is shown .
developer_mode = 0

while True:

    if flag == "main_menu":
        flag, developer_mode = main_menu()

    if flag == "map01":
        flag, x_pos, y_pos = map01(x_pos, y_pos, developer_mode)

    if flag == "map02":
        flag, x_pos, y_pos = map02(x_pos, y_pos, developer_mode)

    if flag == "map03":
        flag, x_pos, y_pos = map03(x_pos, y_pos, developer_mode)

    if flag == "map04":
        flag, x_pos, y_pos = map04(x_pos, y_pos, developer_mode)

    if flag == "game_over":
        flag = game_over()
