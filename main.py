from GameOver import game_over
from Menu import main_menu
import importlib
import argparse


# define the initial player position for map01
map01_x_pos = 780
map01_y_pos = 390


def main():
    args = parse_args()

    level_id = "main_menu"
    x_pos, y_pos = 0, 0
    while True:
        level_id, x_pos, y_pos = play_level(
            level_id, x_pos, y_pos, args.developer_mode)


# Parse command line arguments and return args
def parse_args():
    parser = argparse.ArgumentParser(description="Run the game")
    parser.add_argument(
        "--developer-mode",
        action="store_true",
        help="Enable developer mode. When enabled, "
        "additional information useful for debugging or development is shown "
             "(e.g., display map positions, hit boxes)",
    )
    args = parser.parse_args()
    return args


# Play the level with the given level_id and player position and return
# the next level_id and player position
def play_level(level_id, x_pos, y_pos, developer_mode):
    if level_id == "main_menu":
        level_id, _ = main_menu()
    elif level_id == "game_over":
        level_id = game_over()
    else:
        if level_id == "map01":
            x_pos, y_pos = map01_x_pos, map01_y_pos

        map_module = importlib.import_module(level_id.title())
        map_function = map_module.__getattribute__(level_id)
        level_id, x_pos, y_pos = map_function(
            x_pos, y_pos, developer_mode)

    return level_id, x_pos, y_pos


if __name__ == "__main__":
    main()
