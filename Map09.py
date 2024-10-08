import random
import time
import pygame
import os
from Ground import Ground
from MyPlayer import MyPlayer
from Wall import Wall
from InvisibleWall import InvisibleWall

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))


def map09(x_pos, y_pos, developer_mode):
    # start the pygame and pygame mixer
    pygame.init()
    pygame.mixer.init()

    # Native resolution of the map
    map_width = 1536
    map_height = 864
    map_aspect_ratio = map_width / map_height

    # Get screen resolution
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    screen_aspect_ratio = screen_width / screen_height

    if screen_aspect_ratio >= map_aspect_ratio:
        scale_factor = screen_height / map_height
        scaled_width = int(map_width * scale_factor)
        scaled_height = screen_height
        offset_x = (screen_width - scaled_width) // 2
        offset_y = 0
    else:
        scale_factor = screen_width / map_width
        scaled_width = screen_width
        scaled_height = int(map_height * scale_factor)
        offset_x = 0
        offset_y = (screen_height - scaled_height) // 2

    # Create a scaled surface
    scaled_surface = pygame.Surface((map_width, map_height))

    # Set up the screen to full resolution
    pygame.display.set_caption('Prison Escape')
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Hide the mouse cursor
    if not developer_mode:
        pygame.mouse.set_visible(False)

    # flag for toggle between player view and developer view
    view_toggle = True

    # load texture
    ground_texture = pygame.image.load(os.path.join(base_dir, 'assets/map09/ground/ground.jpg'))

    wall_texture = pygame.image.load(os.path.join(base_dir, 'assets/map09/wall/wall.png'))

    idle = pygame.image.load(os.path.join(base_dir, 'assets/map09/player/idle.png'))

    walk_up = None

    walk_left = [pygame.image.load(os.path.join(base_dir, 'assets/map09/player/L1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map09/player/L2.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map09/player/L3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map09/player/L4.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map09/player/L5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map09/player/L6.png'))]

    walk_down = None

    walk_right = [pygame.image.load(os.path.join(base_dir, 'assets/map09/player/R1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map09/player/R2.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map09/player/R3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map09/player/R4.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map09/player/R5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map09/player/R6.png'))]

    # define the ground
    ground = Ground(map_width, map_height, ground_texture)

    # Create the player character
    # The player is represented by an instance of the MyPlayer class:
    # - (x_pos, y_pos): Initial position on the screen
    # - screen: Pygame screen object
    # - Textures for different directions (walk_up, walk_left, walk_down, walk_right, idle)
    # - Speed (5th input): Controls how fast the player moves (higher values mean faster movement)
    # - developer_mode: A flag indicating whether to enable developer-specific features
    player = MyPlayer(x_pos, y_pos, scaled_surface, walk_up, walk_left, walk_down, walk_right, idle, 5, developer_mode)

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 1535, 60, wall_texture), Wall(0, 60, 120, 210, wall_texture),
             Wall(60, 240, 60, 30, wall_texture), Wall(60, 300, 30, 30, wall_texture),
             Wall(0, 300, 90, 480, wall_texture), Wall(120, 60, 60, 690, wall_texture),
             Wall(210, 90, 60, 690, wall_texture), Wall(300, 60, 60, 690, wall_texture),
             Wall(390, 90, 60, 690, wall_texture), Wall(480, 60, 60, 690, wall_texture),
             Wall(570, 90, 60, 690, wall_texture), Wall(660, 60, 60, 690, wall_texture),
             Wall(750, 90, 60, 690, wall_texture), Wall(840, 60, 60, 690, wall_texture),
             Wall(930, 90, 60, 690, wall_texture), Wall(1020, 60, 60, 690, wall_texture),
             Wall(1110, 90, 60, 690, wall_texture), Wall(1200, 60, 60, 690, wall_texture),
             Wall(1290, 90, 60, 690, wall_texture), Wall(1380, 60, 60, 690, wall_texture),
             Wall(1440, 60, 95, 390, wall_texture), Wall(1440, 420, 60, 30, wall_texture),
             Wall(1470, 480, 30, 30, wall_texture), Wall(1470, 480, 65, 300, wall_texture),
             Wall(0, 780, 1535, 83, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(1533, 420, 2, 90), InvisibleWall(0, 240, 2, 90)]

    # Buttons that trigger the wall spawning mechanism when the player collides with them :
    # - The first button is for when the player moves from the left side of the map to the right.
    # - The second button is for when the player moves from the right side of the map to the left.
    triggers = [InvisibleWall(180, 270, 30, 30), InvisibleWall(1350, 450, 30, 30)]

    # Walls defined before appending them to the killer wall list
    walls_append = [Wall(0, 0, 30, 864, wall_texture), Wall(30, 0, 30, 864, wall_texture),
                    Wall(60, 0, 30, 864, wall_texture), Wall(90, 0, 30, 864, wall_texture),
                    Wall(120, 0, 30, 864, wall_texture), Wall(150, 0, 30, 864, wall_texture),
                    Wall(180, 0, 30, 864, wall_texture), Wall(210, 0, 30, 864, wall_texture),
                    Wall(240, 0, 30, 864, wall_texture), Wall(270, 0, 30, 864, wall_texture),
                    Wall(300, 0, 30, 864, wall_texture), Wall(330, 0, 30, 864, wall_texture),
                    Wall(360, 0, 30, 864, wall_texture), Wall(390, 0, 30, 864, wall_texture),
                    Wall(420, 0, 30, 864, wall_texture), Wall(450, 0, 30, 864, wall_texture),
                    Wall(480, 0, 30, 864, wall_texture), Wall(510, 0, 30, 864, wall_texture),
                    Wall(540, 0, 30, 864, wall_texture), Wall(570, 0, 30, 864, wall_texture),
                    Wall(600, 0, 30, 864, wall_texture), Wall(630, 0, 30, 864, wall_texture),
                    Wall(660, 0, 30, 864, wall_texture), Wall(690, 0, 30, 864, wall_texture),
                    Wall(720, 0, 30, 864, wall_texture), Wall(750, 0, 30, 864, wall_texture),
                    Wall(780, 0, 30, 864, wall_texture), Wall(810, 0, 30, 864, wall_texture),
                    Wall(840, 0, 30, 864, wall_texture), Wall(870, 0, 30, 864, wall_texture),
                    Wall(900, 0, 30, 864, wall_texture), Wall(930, 0, 30, 864, wall_texture),
                    Wall(960, 0, 30, 864, wall_texture), Wall(990, 0, 30, 864, wall_texture),
                    Wall(1020, 0, 30, 864, wall_texture), Wall(1050, 0, 30, 864, wall_texture),
                    Wall(1080, 0, 30, 864, wall_texture), Wall(1110, 0, 30, 864, wall_texture),
                    Wall(1140, 0, 30, 864, wall_texture), Wall(1170, 0, 30, 864, wall_texture),
                    Wall(1200, 0, 30, 864, wall_texture), Wall(1230, 0, 30, 864, wall_texture),
                    Wall(1260, 0, 30, 864, wall_texture), Wall(1290, 0, 30, 864, wall_texture),
                    Wall(1320, 0, 30, 864, wall_texture), Wall(1350, 0, 30, 864, wall_texture),
                    Wall(1380, 0, 30, 864, wall_texture), Wall(1410, 0, 30, 864, wall_texture),
                    Wall(1440, 0, 30, 864, wall_texture), Wall(1470, 0, 30, 864, wall_texture),
                    Wall(1500, 0, 30, 864, wall_texture), Wall(1530, 0, 36, 864, wall_texture)]

    # Define an empty list for killer walls that can kill the player
    killer_walls = []

    # Trigger variable for activating the wall spawning mechanism:
    trigger = 0

    # Count variable for wall spawning
    clk_for_walls = 0

    # Speed of wall spawn
    speed_of_walls = 55

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # clear screen
        scaled_surface.fill((0, 0, 0))

        ground.draw(scaled_surface)

        # key press for player
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            exit()

        player.move(key)

        # Draw the walls
        for wall in walls:
            wall.draw(scaled_surface)

        # Draw the killer walls
        for wall in killer_walls:
            wall.draw(scaled_surface)

        # Check for player collisions with killer walls
        for killer_wall in killer_walls:
            # if player collide killer walls it goes to game over screen and pass player position of map01 for new start
            if player.rect.colliderect(killer_wall.rect):
                sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map09/sound/lose.wav'))
                sound_effect.set_volume(0.2)
                sound_effect.play()
                pygame.mixer.music.stop()
                return "game_over", 780, 390

        # Handle triggers:
        # - If the player collides with the first trigger, set the trigger variable to 1 and clear the triggers list.
        # - If the player collides with the second trigger, set the trigger variable to 2 and clear the triggers list.
        if triggers and player.rect.colliderect(triggers[0]):
            trigger = 1
            triggers.clear()

        if triggers and player.rect.colliderect(triggers[1]):
            trigger = 2
            triggers.clear()

        # Wall spawning logic:
        # - When trigger is 1 (player on the left), spawn walls from the left.
        # - When clk_for_walls % speed_of_walls becomes 0, append the first wall from the walls_append list
        #   to killer walls and remove it from walls_append.
        if trigger == 1:
            clk_for_walls += 1
            if (clk_for_walls % speed_of_walls) == 0 and walls_append:
                killer_walls.append(walls_append[0])
                walls_append.remove(walls_append[0])
                sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map09/sound/place.wav'))
                sound_effect.set_volume(0.2)
                sound_effect.play()

        # - When trigger is 2 (player on the right), spawn walls from the right.
        # - When clk_for_walls % speed_of_walls becomes 0, append the last wall from the walls_append list
        #   to killer walls and remove it from walls_append.
        if trigger == 2:
            clk_for_walls += 1
            if (clk_for_walls % speed_of_walls) == 0 and walls_append:
                killer_walls.append(walls_append[-1])
                walls_append.remove(walls_append[-1])
                sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map09/sound/place.wav'))
                sound_effect.set_volume(0.2)
                sound_effect.play()

        # player collide check with walls
        player.check_collision(walls)

        # Developer Mode Options:
        # - Display map number
        # - Show mouse position on screen
        # - Show player X and Y coordinates
        # - Show bounding rectangles of all objects when developer view is enabled
        # - Teleport player to mouse position when the space key is pressed
        # - Toggle between player view and developer view using the left-alt key
        if developer_mode:
            font = pygame.font.SysFont("", 24)

            # Get the scaled mouse position
            scaled_mouse_x = (pygame.mouse.get_pos()[0] - offset_x) / scale_factor
            scaled_mouse_y = (pygame.mouse.get_pos()[1] - offset_y) / scale_factor

            # Display developer information on the scaled surface
            scaled_surface.blit(font.render(f"Developer Mode - Map09", True, (255, 0, 0)), (10, 5))
            scaled_surface.blit(font.render(f'X: {scaled_mouse_x:.0f}, Y: {scaled_mouse_y:.0f}', True, (255, 0, 0)),
                                (10, 25))
            scaled_surface.blit(font.render(f'player x : {player.x}', True, (255, 0, 0)), (10, 45))
            scaled_surface.blit(font.render(f'player y : {player.y}', True, (255, 0, 0)), (10, 65))

            # Teleport player to scaled mouse position when the space key is pressed
            if key[pygame.K_SPACE]:
                player.x = scaled_mouse_x
                player.y = scaled_mouse_y

            if key[pygame.K_LALT]:
                time.sleep(0.2)
                if not view_toggle:
                    view_toggle = True
                else:
                    view_toggle = False

            if view_toggle:
                scaled_surface.blit(font.render('Developer View', True, (255, 0, 0)), (10, 85))
                player.draw_rect(scaled_surface)

                for mp_dev in mp:
                    mp_dev.draw(scaled_surface, (0, 0, 255))

                for wall in walls:
                    wall.rect_draw(scaled_surface, (0, 255, 0))

                for trig in triggers:
                    trig.draw(scaled_surface, (0, 0, 255))

            if not view_toggle:
                scaled_surface.blit(font.render('Player View', True, (255, 0, 0)), (10, 85))

        # Draw the scaled surface on the screen with scaling and centering
        screen.fill((0, 0, 0))
        scaled_screen = pygame.transform.scale(scaled_surface, (scaled_width, scaled_height))
        screen.blit(scaled_screen, (offset_x, offset_y))

        # Frame rate
        pygame.time.Clock().tick(240)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[0]):
            return "map02", 3, random.randint(421, 481)

        if player.rect.colliderect(mp[1]):
            return "map21", 1507, 277

        # update display
        pygame.display.flip()

    pygame.quit()
