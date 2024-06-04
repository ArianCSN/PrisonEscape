import random

import pygame
from Ground import Ground
from MyPlayer import MyPlayer
from Wall import Wall
from InvisibleWall import InvisibleWall
import time

def map16(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load('assets/map16/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map16/wall/wall.png')

    idle = pygame.image.load('assets/map16/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map16/player/L1.png'), pygame.image.load('assets/map16/player/L2.png'),
                 pygame.image.load('assets/map16/player/L3.png'), pygame.image.load('assets/map16/player/L4.png'),
                 pygame.image.load('assets/map16/player/L5.png'), pygame.image.load('assets/map16/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map16/player/R1.png'), pygame.image.load('assets/map16/player/R2.png'),
                  pygame.image.load('assets/map16/player/R3.png'), pygame.image.load('assets/map16/player/R4.png'),
                  pygame.image.load('assets/map16/player/R5.png'), pygame.image.load('assets/map16/player/R6.png')]

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
    walls = [Wall(0, 0, 720, 240, wall_texture), Wall(840, 0, 696, 240, wall_texture),
             Wall(0, 360, 360, 240, wall_texture), Wall(1200, 360, 336, 240, wall_texture),
             Wall(360, 360, 60, 504, wall_texture), Wall(1140, 360, 60, 504, wall_texture),
             Wall(0, 720, 240, 144, wall_texture), Wall(1320, 720, 216, 144, wall_texture),
             Wall(420, 630, 300, 234, wall_texture), Wall(840, 630, 300, 234, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(720, 0, 120, 2), InvisibleWall(1534, 240, 2, 120),
          InvisibleWall(1534, 600, 2, 120), InvisibleWall(1200, 862, 120, 2),
          InvisibleWall(720, 862, 120, 2), InvisibleWall(240, 862, 120, 2),
          InvisibleWall(0, 600, 2, 120), InvisibleWall(0, 240, 2, 120)]

    # Teleports that teleports you
    # These rects act as triggers to teleport from one point to another :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - Teleports objects handle teleportation
    tps = [InvisibleWall(690, 390, 180, 120)]

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

        # Draw the walls
        for wall in walls:
            wall.draw(screen)

        # Draw the Teleport Areas
        for tp in tps:
            tp.draw(screen, (111, 49, 152))

        # initialized the font
        font = pygame.font.SysFont("", 24)

        # Text lines for the teleportation room description
        teleport_lines = [
            "Teleportation Room",
            "You can use the teleporter in this room to randomly teleport.",
            "There's a 4% chance of instant death upon teleportation.",
            "Additionally, there's a 4% chance of teleporting to an exit room."
        ]

        # Blit the text lines onto the screen
        for i, line in enumerate(teleport_lines):
            screen.blit(font.render(line, True, (255, 0, 0)), (454, 260 + i * 20))

        # Teleportation Logic
        if player.rect.colliderect(tps[0]):
            # Play teleportation sound effect
            sound_effect = pygame.mixer.Sound('assets/map16/sound/teleport.wav')
            sound_effect.set_volume(1)
            sound_effect.play()

            # Create a white flash effect (you can adjust the duration and intensity)
            flash_surface = pygame.Surface(screen.get_size())
            flash_surface.fill((255, 255, 255))  # White color
            flash_surface.set_alpha(100)  # Adjust transparency (0 to 255)
            screen.blit(flash_surface, (0, 0))
            pygame.display.flip()

            random_tp = [
                ["map01", 66, 390],
                ["map02", 224, 449],
                ["map03", 1087, 860],
                ["map04", 1417, 220],
                ["map05", 32, 370],
                ["map06", 1265, 144],
                ["map07", 807, 800],
                ["map08", 23, 106],
                ["map09", 20, 274],
                ["map10", 257, 283],
                ["map11", 1052, 405],
                ["map12", 1322, 641],
                ["map13", 813, 575],
                ["map14", 755, 305],
                ["map15", 721, 124]
            ]
            return random.choice(random_tp)


        # player collide check with walls
        player.check_collision(walls)

        # Options for developer mode:
        # - Show map number
        # - Show position of mouse and player on screen
        # - Show player, map changers, walls and bots rect
        # - If the space key is pressed, the player teleports to the mouse position
        if developer_mode:
            x, y = pygame.mouse.get_pos()
            screen.blit(font.render(f"Developer Mode - map16", True, (255, 0, 0)), (10, 5))
            screen.blit(font.render(f'X: {x}, Y: {y}', True, (255, 0, 0)), (10, 25))
            screen.blit(font.render(f'player x : {player.x}', True, (255, 0, 0)), (10, 45))
            screen.blit(font.render(f'player y : {player.y}', True, (255, 0, 0)), (10, 65))

            if key[pygame.K_SPACE]:
                player.x = x
                player.y = y

            player.draw_rect(screen)

            for mp_dev in mp:
                mp_dev.draw(screen, (0, 0, 255))

            for wall in walls:
                wall.rect_draw(screen, (0, 255, 0))

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        # Due to differentiation in player texture length between map03 and other maps
        # subtract from player's x position to ensure no collision with the wall occurs.
        if player.rect.colliderect(mp[0]):
            if player.x > 776:
                player.x -= 9
            return "map04", player.x, 826

        if player.rect.colliderect(mp[1]):
            if player.y > 300:
                player.y -= 1
            return "map12", 3, player.y

        if player.rect.colliderect(mp[2]):
            if player.y > 660:
                player.y -= 1
            return "map12", 3, player.y

        # update display
        pygame.display.flip()

    pygame.quit()
