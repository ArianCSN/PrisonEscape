import pygame
import time
from Ground import Ground
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from InvisibleWall import InvisibleWall


def map01(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load('assets/map01/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map01/wall/wall.png')

    idle = pygame.image.load('assets/map01/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map01/player/L1.png'), pygame.image.load('assets/map01/player/L2.png'),
                 pygame.image.load('assets/map01/player/L3.png'), pygame.image.load('assets/map01/player/L4.png'),
                 pygame.image.load('assets/map01/player/L5.png'), pygame.image.load('assets/map01/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map01/player/R1.png'), pygame.image.load('assets/map01/player/R2.png'),
                  pygame.image.load('assets/map01/player/R3.png'), pygame.image.load('assets/map01/player/R4.png'),
                  pygame.image.load('assets/map01/player/R5.png'), pygame.image.load('assets/map01/player/R6.png')]

    bot_idle = pygame.image.load('assets/map01/bot/bot1/idle.png')

    bot_up = None

    bot_left = [pygame.image.load('assets/map01/bot/bot1/L1.png'), pygame.image.load('assets/map01/bot/bot1/L2.png'),
                pygame.image.load('assets/map01/bot/bot1/L3.png'), pygame.image.load('assets/map01/bot/bot1/L4.png'),
                pygame.image.load('assets/map01/bot/bot1/L5.png'), pygame.image.load('assets/map01/bot/bot1/L6.png')]

    bot_down = None

    bot_right = [pygame.image.load('assets/map01/bot/bot1/R1.png'), pygame.image.load('assets/map01/bot/bot1/R2.png'),
                 pygame.image.load('assets/map01/bot/bot1/R3.png'), pygame.image.load('assets/map01/bot/bot1/R4.png'),
                 pygame.image.load('assets/map01/bot/bot1/R5.png'), pygame.image.load('assets/map01/bot/bot1/R6.png')]

    bot2_idle = pygame.image.load('assets/map01/bot/bot2/idle.png')

    bot2_up = None

    bot2_left = [pygame.image.load('assets/map01/bot/bot2/L1.png'), pygame.image.load('assets/map01/bot/bot2/L2.png'),
                 pygame.image.load('assets/map01/bot/bot2/L3.png'), pygame.image.load('assets/map01/bot/bot2/L4.png'),
                 pygame.image.load('assets/map01/bot/bot2/L5.png'), pygame.image.load('assets/map01/bot/bot2/L6.png')]

    bot2_down = None

    bot2_right = [pygame.image.load('assets/map01/bot/bot2/R1.png'), pygame.image.load('assets/map01/bot/bot2/R2.png'),
                  pygame.image.load('assets/map01/bot/bot2/R3.png'), pygame.image.load('assets/map01/bot/bot2/R4.png'),
                  pygame.image.load('assets/map01/bot/bot2/R5.png'), pygame.image.load('assets/map01/bot/bot2/R6.png')]

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

    # Define the bots
    # Each bot is initialized with specific parameters:
    # - (x, y): Initial position on the screen
    # - screen: Pygame screen object
    # - Textures for different directions (up, left, down, right, idle)
    # - Speed (9th input): Controls how fast the bot moves (higher values mean faster movement)
    # - developer_mode: A flag indicating whether to enable developer-specific features
    bots = [Bot(200, 90, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(240, 480, screen, bot2_up, bot2_left, bot2_down, bot2_right, bot2_idle, 1, developer_mode),
            Bot(630, 420, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(540, 750, screen, bot2_up, bot2_left, bot2_down, bot2_right, bot2_idle, 1, developer_mode),
            Bot(1320, 400, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(990, 230, screen, bot2_up, bot2_left, bot2_down, bot2_right, bot2_idle, 1, developer_mode)]

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 750, 60, wall_texture), Wall(0, 60, 60, 300, wall_texture),
             Wall(170, 150, 180, 90, wall_texture), Wall(60, 300, 150, 60, wall_texture),
             Wall(120, 360, 90, 270, wall_texture), Wall(0, 450, 60, 413, wall_texture),
             Wall(60, 690, 210, 113, wall_texture), Wall(60, 803, 390, 60, wall_texture),
             Wall(300, 180, 150, 570, wall_texture), Wall(390, 600, 360, 90, wall_texture),
             Wall(450, 450, 90, 240, wall_texture), Wall(450, 833, 180, 30, wall_texture),
             Wall(540, 210, 180, 150, wall_texture), Wall(720, 270, 30, 60, wall_texture),
             Wall(720, 270, 450, 60, wall_texture), Wall(870, 330, 300, 90, wall_texture),
             Wall(630, 480, 420, 120, wall_texture), Wall(630, 600, 120, 150, wall_texture),
             Wall(840, 0, 695, 180, wall_texture), Wall(1260, 180, 275, 180, wall_texture),
             Wall(630, 803, 120, 60, wall_texture), Wall(840, 683, 695, 180, wall_texture),
             Wall(1110, 420, 60, 90, wall_texture), Wall(1050, 570, 240, 30, wall_texture),
             Wall(1170, 450, 300, 60, wall_texture), Wall(1350, 510, 120, 120, wall_texture),
             Wall(1500, 450, 35, 235, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(750, 0, 90, 2), InvisibleWall(1535, 360, 2, 90),
          InvisibleWall(750, 863, 90, 2), InvisibleWall(0, 360, 2, 90)]

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

        # Draw the bots
        for bot in bots:
            bot.move()
            bot.check_collision(walls)
            bot.check_collision(mp)
            # if player collide bots it goes to game over screen and pass player position of map01 for new start
            if player.rect.colliderect(bot.rect):
                sound_effect = pygame.mixer.Sound('assets/map01/sound/lose.wav')
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
            x, y = pygame.mouse.get_pos()
            screen.blit(font.render(f"Developer Mode - Map01", True, (255, 0, 0)), (10, 5))
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

                for bot in bots:
                    bot.draw_rect(screen)

                for mp_dev in mp:
                    mp_dev.draw(screen, (0, 0, 255))

                for wall in walls:
                    wall.rect_draw(screen, (0, 255, 0))

            if not view_toggle:
                screen.blit(font.render('Player View', True, (255, 0, 0)), (10, 85))

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        # Due to differentiation in player texture length between map01 and other maps
        # subtract from player's x position to ensure no collision with the wall occurs.
        if player.rect.colliderect(mp[0]):
            if player.x > 793:
                player.x -= 20
            return "map02", player.x, 835

        if player.rect.colliderect(mp[1]):
            if player.y > 831:
                player.y -= 2
            return "map03", 3, player.y

        if player.rect.colliderect(mp[2]):
            if player.x > 793:
                player.x -= 11
            return "map04", player.x, 2

        if player.rect.colliderect(mp[3]):
            return "map05", 1500, player.y

        # update display
        pygame.display.flip()

    pygame.quit()
