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

    # set up screen
    screen_width = 1536
    screen_height = 864
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
    ground = Ground(screen_width, screen_height, ground_texture)

    # Create the player character
    # The player is represented by an instance of the MyPlayer class:
    # - (x_pos, y_pos): Initial position on the screen
    # - screen: Pygame screen object
    # - Textures for different directions (walk_up, walk_left, walk_down, walk_right, idle)
    # - Speed (5th input): Controls how fast the player moves (higher values mean faster movement)
    # - developer_mode: A flag indicating whether to enable developer-specific features
    player = MyPlayer(x_pos, y_pos, screen, walk_up, walk_left, walk_down, walk_right, idle, 5, developer_mode)

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
        screen.fill((0, 0, 0))

        ground.draw(screen)

        # key press for player
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            exit()

        player.move(key)

        # player collide check with walls
        player.check_collision(walls)

        # Draw the walls , map changers , buttons and doors
        for wall in walls:
            wall.draw(screen)

        for mp_dev in mp:
            mp_dev.draw(screen, (0, 0, 255))

        # Developer Mode Options:
        # - Display map number
        # - Show mouse position on screen
        # - Show player X and Y coordinates
        # - Show bounding rectangles of all objects when developer view is enabled
        # - Teleport player to mouse position when the space key is pressed
        # - Toggle between player view and developer view using the left-alt key
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            screen.blit(font.render(f"Developer Mode - map14", True, (255, 0, 0)), (10, 5))
            screen.blit(font.render(f'X: {x}, Y: {y}', True, (255, 0, 0)), (10, 25))
            screen.blit(font.render(f'player x : {player.x}', True, (255, 0, 0)), (10, 45))
            screen.blit(font.render(f'player y : {player.y}', True, (255, 0, 0)), (10, 65))

            if key[pygame.K_SPACE]:
                player.x = x
                player.y = y

            if key[pygame.K_LALT]:
                time.sleep(0.2)
                if not view_toggle:
                    view_toggle = True
                else:
                    view_toggle = False

            if view_toggle:
                screen.blit(font.render('Developer View', True, (255, 0, 0)), (10, 85))
                player.draw_rect(screen)

                for wall in walls:
                    wall.rect_draw(screen, (0, 255, 0))

            if not view_toggle:
                screen.blit(font.render('Player View', True, (255, 0, 0)), (10, 85))

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
