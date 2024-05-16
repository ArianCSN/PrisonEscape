import pygame
from Ground import Ground
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from InvisibleWall import InvisibleWall


def map05(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load('assets/map05/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map05/wall/wall.png')

    idle = pygame.image.load('assets/map05/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map05/player/L1.png'), pygame.image.load('assets/map05/player/L2.png'),
                 pygame.image.load('assets/map05/player/L3.png'), pygame.image.load('assets/map05/player/L4.png'),
                 pygame.image.load('assets/map05/player/L5.png'), pygame.image.load('assets/map05/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map05/player/R1.png'), pygame.image.load('assets/map05/player/R2.png'),
                  pygame.image.load('assets/map05/player/R3.png'), pygame.image.load('assets/map05/player/R4.png'),
                  pygame.image.load('assets/map05/player/R5.png'), pygame.image.load('assets/map05/player/R6.png')]

    bot_idle = pygame.image.load('assets/map05/bot/idle.png')

    bot_up = None

    bot_left = [pygame.image.load('assets/map05/bot/L1.png'), pygame.image.load('assets/map05/bot/L2.png'),
                pygame.image.load('assets/map05/bot/L3.png'), pygame.image.load('assets/map05/bot/L4.png'),
                pygame.image.load('assets/map05/bot/L5.png'), pygame.image.load('assets/map05/bot/L6.png')]

    bot_down = None

    bot_right = [pygame.image.load('assets/map05/bot/R1.png'), pygame.image.load('assets/map05/bot/R2.png'),
                 pygame.image.load('assets/map05/bot/R3.png'), pygame.image.load('assets/map05/bot/R4.png'),
                 pygame.image.load('assets/map05/bot/R5.png'), pygame.image.load('assets/map05/bot/R6.png')]

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
    bots = [Bot(300, 210, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(660, 180, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(990, 210, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(180, 600, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(990, 600, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(1290, 600, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            # bots in the middle
            Bot(150, 360, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(300, 390, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(450, 420, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(600, 390, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(750, 360, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(900, 390, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(1050, 420, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode)]

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 1535, 150, wall_texture), Wall(0, 270, 1380, 60, wall_texture),
             Wall(0, 480, 1380, 60, wall_texture), Wall(0, 660, 450, 203, wall_texture),
             Wall(570, 540, 120, 323, wall_texture), Wall(1500, 150, 35, 210, wall_texture),
             Wall(1320, 330, 60, 150, wall_texture), Wall(1500, 450, 35, 210, wall_texture),
             Wall(810, 660, 725, 203, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(1533, 360, 2, 90), InvisibleWall(690, 861, 120, 2),
          InvisibleWall(450, 861, 120, 2), InvisibleWall(0, 540, 2, 120),
          InvisibleWall(0, 330, 2, 150), InvisibleWall(0, 150, 2, 120)]

    # Teleports that teleports you
    # These rects act as triggers to teleport from one point to another :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - Teleports objects handle teleportation
    tps = [InvisibleWall(1290, 330, 30, 150)]

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

        # Teleportation Logic
        # if player.rect.colliderect(tps[0]):
        #     # Check player's x-coordinate
        #     if player.x < 695:
        #         TheX = player.x - 515
        #     else:
        #         TheX = player.x - 522
        #
        #     # Calculate new y-coordinate after teleportation
        #     player.y = 65 + TheX
        #     player.x = 1386
        #
        #     # Play teleportation sound effect
        #     sound_effect = pygame.mixer.Sound('assets/map05/sound/teleport.wav')
        #     sound_effect.set_volume(0.2)
        #     sound_effect.play()

        # Draw the bots
        for bot in bots:
            bot.move()
            bot.check_collision(walls)
            bot.check_collision(tps)
            bot.check_collision(mp)
            # if player collide bots it goes to game over screen and pass player position of map01 for new start
            if player.rect.colliderect(bot.rect):
                sound_effect = pygame.mixer.Sound('assets/map05/sound/lose.wav')
                sound_effect.set_volume(0.2)
                sound_effect.play()
                pygame.mixer.music.stop()
                return "game_over", 780, 390

        # player collide check with walls
        player.check_collision(walls)

        # options for developer mode
        # show position of mouse on screen
        # show player and bots rect and also hidden map changer with blue color
        # If the space key is pressed, the player teleport to mouse position
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            coord_text = font.render(f'X: {x}, Y: {y}', True, (255, 0, 0))
            screen.blit(coord_text, (10, 10))  # Draw the text

            if key[pygame.K_SPACE]:
                player.x = x
                player.y = y

            player.draw_rect(screen)
            for bot in bots:
                bot.draw_rect(screen)
            for mp_dev in mp:
                mp_dev.draw(screen, (0, 0, 255))

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[0]):
            return "map01", 3, player.y

        # update display
        pygame.display.flip()

    pygame.quit()
