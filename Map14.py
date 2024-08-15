import pygame
import time
import random
from Ground import Ground
from MyPlayer import MyPlayer
from Wall import Wall
from InvisibleWall import InvisibleWall


def map14(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load('assets/map14/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map14/wall/wall.png')

    idle = pygame.image.load('assets/map14/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map14/player/L1.png'), pygame.image.load('assets/map14/player/L2.png'),
                 pygame.image.load('assets/map14/player/L3.png'), pygame.image.load('assets/map14/player/L4.png'),
                 pygame.image.load('assets/map14/player/L5.png'), pygame.image.load('assets/map14/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map14/player/R1.png'), pygame.image.load('assets/map14/player/R2.png'),
                  pygame.image.load('assets/map14/player/R3.png'), pygame.image.load('assets/map14/player/R4.png'),
                  pygame.image.load('assets/map14/player/R5.png'), pygame.image.load('assets/map14/player/R6.png')]

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

    # Adjust the player's rectangle size to prevent it from getting stuck at the edges
    player.rect = pygame.Rect(x_pos, y_pos, 20, 22)

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 1536, 90, wall_texture), Wall(0, 90, 750, 210, wall_texture),
             Wall(780, 90, 756, 210, wall_texture), Wall(0, 300, 90, 30, wall_texture),
             Wall(1470, 300, 90, 30, wall_texture), Wall(0, 330, 750, 420, wall_texture),
             Wall(780, 330, 756, 420, wall_texture), Wall(0, 750, 1536, 114, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(750, 90, 30, 30), InvisibleWall(1440, 300, 30, 30),
          InvisibleWall(750, 720, 30, 30), InvisibleWall(90, 300, 30, 30)]

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

        # player collide check with walls
        player.check_collision(walls)

        # Draw the walls , map changers , buttons and doors
        for wall in walls:
            wall.draw(scaled_surface)

        for mp_dev in mp:
            mp_dev.draw(scaled_surface, (0, 0, 255))

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
            scaled_surface.blit(font.render(f"Developer Mode - Map14", True, (255, 0, 0)), (10, 5))
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

                for wall in walls:
                    wall.rect_draw(scaled_surface, (0, 255, 0))

            if not view_toggle:
                scaled_surface.blit(font.render('Player View', True, (255, 0, 0)), (10, 85))

        # Draw the scaled surface on the screen with scaling and centering
        screen.fill((0, 0, 0))
        scaled_screen = pygame.transform.scale(scaled_surface, (scaled_width, scaled_height))
        screen.blit(scaled_screen, (offset_x, offset_y))

        # Frame rate
        pygame.time.Clock().tick(60)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[1]):
            return "map18", 3, random.randint(302, 472)

        if player.rect.colliderect(mp[2]):
            return "map02", 1208, 3

        if player.rect.colliderect(mp[3]):
            return "map10", 1511, 670

        # update display
        pygame.display.flip()

    pygame.quit()
