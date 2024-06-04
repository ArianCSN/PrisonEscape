import pygame
from Ground import Ground
from MyPlayer import MyPlayer
from Wall import Wall
from InvisibleWall import InvisibleWall
import random

def map15(x_pos, y_pos, developer_mode):
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

    # load texture
    ground_texture = pygame.image.load('assets/map15/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map15/wall/wall.png')

    idle = pygame.image.load('assets/map15/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map15/player/L1.png'), pygame.image.load('assets/map15/player/L2.png'),
                 pygame.image.load('assets/map15/player/L3.png'), pygame.image.load('assets/map15/player/L4.png'),
                 pygame.image.load('assets/map15/player/L5.png'), pygame.image.load('assets/map15/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map15/player/R1.png'), pygame.image.load('assets/map15/player/R2.png'),
                  pygame.image.load('assets/map15/player/R3.png'), pygame.image.load('assets/map15/player/R4.png'),
                  pygame.image.load('assets/map15/player/R5.png'), pygame.image.load('assets/map15/player/R6.png')]

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

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 300, 600, wall_texture), Wall(0, 600, 120, 264, wall_texture),
             Wall(120, 630, 180, 234, wall_texture), Wall(300, 0, 1236, 60, wall_texture),
             Wall(330, 60, 1206, 60, wall_texture), Wall(330, 120, 390, 630, wall_texture),
             Wall(300, 780, 1236, 84, wall_texture), Wall(750, 150, 660, 450, wall_texture),
             Wall(750, 600, 630, 90, wall_texture), Wall(720, 690, 660, 60, wall_texture),
             Wall(1410, 120, 126, 660, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(300, 60, 30, 30), InvisibleWall(723, 119, 30, 1),
          InvisibleWall(1380, 120, 30, 30), InvisibleWall(1380, 600, 30, 30),
           InvisibleWall(720, 660, 30, 30), InvisibleWall(120, 600, 30, 30)]

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

        for mps in mp:
            mps.draw(screen, (0, 0, 255))

        # Options for developer mode:
        # - Show map number
        # - Show position of mouse and player on screen
        # - Show player and walls rect
        # - If the space key is pressed, the player teleports to the mouse position
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            screen.blit(font.render(f"Developer Mode - map15", True, (255, 0, 0)), (10, 5))
            screen.blit(font.render(f'X: {x}, Y: {y}', True, (255, 0, 0)), (10, 25))
            screen.blit(font.render(f'player x : {player.x}', True, (255, 0, 0)), (10, 45))
            screen.blit(font.render(f'player y : {player.y}', True, (255, 0, 0)), (10, 65))

            if key[pygame.K_SPACE]:
                player.x = x
                player.y = y

            player.draw_rect(screen)

            for wall in walls:
                wall.rect_draw(screen, (0, 255, 0))

        # Frame rate
        pygame.time.Clock().tick(60)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[0]):
            return "map11", random.randint(240, 385), 830

        if player.rect.colliderect(mp[1]):
            return "map11", random.randint(992, 1107), 830

        if player.rect.colliderect(mp[5]):
            return "map03", 1508, random.randint(454, 564)

        # update display
        pygame.display.flip()

    pygame.quit()
