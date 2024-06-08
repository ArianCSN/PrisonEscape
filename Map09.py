import random

import pygame
from Ground import Ground
from MyPlayer import MyPlayer
from Wall import Wall
from InvisibleWall import InvisibleWall


def map09(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load('assets/map09/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map09/wall/wall.png')

    idle = pygame.image.load('assets/map09/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map09/player/L1.png'), pygame.image.load('assets/map09/player/L2.png'),
                 pygame.image.load('assets/map09/player/L3.png'), pygame.image.load('assets/map09/player/L4.png'),
                 pygame.image.load('assets/map09/player/L5.png'), pygame.image.load('assets/map09/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map09/player/R1.png'), pygame.image.load('assets/map09/player/R2.png'),
                  pygame.image.load('assets/map09/player/R3.png'), pygame.image.load('assets/map09/player/R4.png'),
                  pygame.image.load('assets/map09/player/R5.png'), pygame.image.load('assets/map09/player/R6.png')]
    
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
                    Wall(60, 0, 30, 864, wall_texture ), Wall(90, 0, 30, 864, wall_texture),
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

        # Draw the killer walls
        for wall in killer_walls:
            wall.draw(screen)

        # Check for player collisions with killer walls
        for killer_wall in killer_walls:
            # if player collide killer walls it goes to game over screen and pass player position of map01 for new start
            if player.rect.colliderect(killer_wall.rect):
                sound_effect = pygame.mixer.Sound('assets/map09/sound/lose.wav')
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
                sound_effect = pygame.mixer.Sound('assets/map09/sound/place.wav')
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
                sound_effect = pygame.mixer.Sound('assets/map09/sound/place.wav')
                sound_effect.set_volume(0.2)
                sound_effect.play()

        # player collide check with walls
        player.check_collision(walls)

        # Options for developer mode:
        # - Show map number
        # - Show position of mouse and player on screen
        # - Show player, map changers, walls, and triggers rect
        # - If the space key is pressed, the player teleports to the mouse position
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            screen.blit(font.render(f"Developer Mode - Map09", True, (255, 0, 0)), (10, 5))
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

            for trig in triggers:
                trig.draw(screen, (0, 0, 255))


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
