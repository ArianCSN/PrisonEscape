import pygame
import random
import time
import os
from Ground import Ground
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from InvisibleWall import InvisibleWall

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))


def map08(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load(os.path.join(base_dir, 'assets/map08/ground/ground.jpg'))

    wall_texture = pygame.image.load(os.path.join(base_dir, 'assets/map08/wall/wall.png'))

    idle = pygame.image.load(os.path.join(base_dir, 'assets/map08/player/idle.png'))

    walk_up = None

    walk_left = [pygame.image.load(os.path.join(base_dir, 'assets/map08/player/L1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/player/L2.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map08/player/L3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/player/L4.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map08/player/L5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/player/L6.png'))]

    walk_down = None

    walk_right = [pygame.image.load(os.path.join(base_dir, 'assets/map08/player/R1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/player/R2.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map08/player/R3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/player/R4.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map08/player/R5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/player/R6.png'))]

    bot_idle = pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/idle.png'))

    bot_up = None

    bot_left = [pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/L1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/L2.png')),
                pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/L3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/L4.png'))]

    bot_down = None

    bot_right = [pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/R1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/R2.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/R3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map08/bot/R4.png'))]

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

    # Bot Spawning Logic
    # - Initializes a list of bots.
    # - Randomly generates between 5 and 15 bots.
    # - Each bot is placed within a specified area:
    #   - x position: random value between 510 and 1117.
    #   - y position: random value between 330 and 720.
    # - Bots are created with textures for different directions (up, left, down, right, idle),
    #   a movement speed of 2, and developer mode settings.
    bots = []

    for i in range(random.randint(5, 15)):
        bots.append(Bot(random.randint(180, 510), random.randint(120, 720), scaled_surface,
                        bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode))

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 450, 60, wall_texture), Wall(0, 180, 120, 480, wall_texture),
             Wall(0, 780, 450, 83, wall_texture), Wall(570, 0, 120, 863, wall_texture),
             Wall(810, 0, 725, 120, wall_texture), Wall(690, 240, 845, 150, wall_texture),
             Wall(810, 510, 120, 353, wall_texture), Wall(930, 510, 605, 120, wall_texture),
             Wall(1050, 750, 485, 173, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(450, 0, 120, 2), InvisibleWall(690, 0, 120, 2),
          InvisibleWall(1535, 120, 2, 120), InvisibleWall(1535, 390, 2, 120),
          InvisibleWall(1535, 630, 2, 120), InvisibleWall(930, 861, 120, 2),
          InvisibleWall(690, 861, 120, 2), InvisibleWall(450, 861, 120, 2),
          InvisibleWall(0, 660, 2, 120), InvisibleWall(0, 60, 2, 120)]

    # Additional border walls:
    # - The player can pass through these borders, but bots are prevented from doing so.
    border = [InvisibleWall(450, 30, 120, 30), InvisibleWall(450, 780, 120, 30),
              InvisibleWall(90, 660, 30, 120), InvisibleWall(90, 60, 30, 120)]

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

        # Draw the bots
        for bot in bots:
            bot.move()
            bot.check_collision(walls)
            bot.check_collision(mp)
            bot.check_collision(border)
            # if player collide bots it goes to game over screen and pass player position of map01 for new start
            if player.rect.colliderect(bot.rect):
                sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map08/sound/lose.wav'))
                sound_effect.set_volume(0.2)
                sound_effect.play()
                pygame.mixer.music.stop()
                return "game_over", 780, 390

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
            scaled_surface.blit(font.render(f"Developer Mode - Map08", True, (255, 0, 0)), (10, 5))
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

                for bot in bots:
                    bot.draw_rect(scaled_surface)

                for mp_dev in mp:
                    mp_dev.draw(scaled_surface, (0, 0, 255))

                for wall in walls:
                    wall.rect_draw(scaled_surface, (0, 255, 0))

                for br in border:
                    br.draw(scaled_surface, (178, 34, 34))

            if not view_toggle:
                scaled_surface.blit(font.render('Player View', True, (255, 0, 0)), (10, 85))

        # Draw the scaled surface on the screen with scaling and centering
        screen.fill((0, 0, 0))
        scaled_screen = pygame.transform.scale(scaled_surface, (scaled_width, scaled_height))
        screen.blit(scaled_screen, (offset_x, offset_y))

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[0]):
            return "map05", player.x, 826

        if player.rect.colliderect(mp[1]):
            return "map05", player.x, 826

        if player.rect.colliderect(mp[2]):
            return "map04", 3, player.y

        if player.rect.colliderect(mp[3]):
            return "map04", 3, player.y

        if player.rect.colliderect(mp[4]):
            return "map04", 3, player.y

        if player.rect.colliderect(mp[5]):
            return "map20", player.x, 3

        if player.rect.colliderect(mp[6]):
            return "map20", player.x, 3

        if player.rect.colliderect(mp[7]):
            return "map20", player.x, 3

        if player.rect.colliderect(mp[8]):
            return "map13", 1440, 720

        if player.rect.colliderect(mp[9]):
            return "map13", 1440, 90

        # update display
        pygame.display.flip()

    pygame.quit()
