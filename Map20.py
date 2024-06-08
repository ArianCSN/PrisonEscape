import pygame
from Ground import Ground
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from InvisibleWall import InvisibleWall


def map20(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load('assets/map20/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map20/wall/wall.png')

    idle = pygame.image.load('assets/map20/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map20/player/L1.png'), pygame.image.load('assets/map20/player/L2.png'),
                 pygame.image.load('assets/map20/player/L3.png'), pygame.image.load('assets/map20/player/L4.png'),
                 pygame.image.load('assets/map20/player/L5.png'), pygame.image.load('assets/map20/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map20/player/R1.png'), pygame.image.load('assets/map20/player/R2.png'),
                  pygame.image.load('assets/map20/player/R3.png'), pygame.image.load('assets/map20/player/R4.png'),
                  pygame.image.load('assets/map20/player/R5.png'), pygame.image.load('assets/map20/player/R6.png')]

    bot_idle = pygame.image.load('assets/map20/bot/idle.png')

    bot_up = None

    bot_left = [pygame.image.load('assets/map20/bot/L1.png'), pygame.image.load('assets/map20/bot/L2.png'),
                pygame.image.load('assets/map20/bot/L3.png'), pygame.image.load('assets/map20/bot/L4.png')]

    bot_down = None

    bot_right = [pygame.image.load('assets/map20/bot/R1.png'), pygame.image.load('assets/map20/bot/R2.png'),
                 pygame.image.load('assets/map20/bot/R3.png'), pygame.image.load('assets/map20/bot/R4.png')]

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
    bots = [Bot(300, 420, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(480, 210, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(480, 630, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(720, 210, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(750, 510, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(980, 240, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(1080, 630, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(1260, 300, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode),
            Bot(1290, 660, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode)]

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 450, 330, wall_texture), Wall(0, 480, 450, 384, wall_texture),
             Wall(570, 0, 120, 864, wall_texture), Wall(810, 0, 120, 480, wall_texture),
             Wall(810, 480, 726, 120, wall_texture), Wall(690, 720, 864, 144, wall_texture),
             Wall(1050, 0, 120, 480, wall_texture), Wall(1170, 0, 364, 240, wall_texture),
             Wall(1290, 360, 270, 120, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(450, 0, 120, 2), InvisibleWall(690, 0, 120, 2),
          InvisibleWall(930, 0, 120, 2), InvisibleWall(1534, 240, 2, 120),
          InvisibleWall(1534, 600, 2, 120), InvisibleWall(1170, 480, 120, 2),
          InvisibleWall(930, 480, 120, 2), InvisibleWall(450, 862, 120, 2),
          InvisibleWall(0, 330, 2, 150)]

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
                sound_effect = pygame.mixer.Sound('assets/map20/sound/lose.wav')
                sound_effect.set_volume(0.2)
                sound_effect.play()
                pygame.mixer.music.stop()
                return "game_over", 780, 390

        # player collide check with walls
        player.check_collision(walls)

        # Options for developer mode:
        # - Show map number
        # - Show position of mouse and player on screen
        # - Show player, map changers, walls and bots rect
        # - If the space key is pressed, the player teleports to the mouse position
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            screen.blit(font.render(f"Developer Mode - map20", True, (255, 0, 0)), (10, 5))
            screen.blit(font.render(f'X: {x}, Y: {y}', True, (255, 0, 0)), (10, 25))
            screen.blit(font.render(f'player x : {player.x}', True, (255, 0, 0)), (10, 45))
            screen.blit(font.render(f'player y : {player.y}', True, (255, 0, 0)), (10, 65))

            if key[pygame.K_SPACE]:
                player.x = x
                player.y = y

            player.draw_rect(screen)

            for bot in bots:
                bot.draw_rect(screen)

            for mp_dev in mp:
                mp_dev.draw(screen, (0, 0, 255))

            for wall in walls:
                wall.rect_draw(screen, (0, 255, 0))

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        # Due to differentiation in player texture length between map20 and other maps
        # subtract from player's x position to ensure no collision with the wall occurs.
        if player.rect.colliderect(mp[0]):
            if player.x > 508:
                player.x -= 20
            return "map08", player.x, 823

        if player.rect.colliderect(mp[1]):
            if player.x > 750:
                player.x -= 20
            return "map08", player.x, 823

        if player.rect.colliderect(mp[2]):
            if player.x > 990:
                player.x -= 20
            return "map08", player.x, 823

        if player.rect.colliderect(mp[3]):
            return "map16", 3, player.y

        if player.rect.colliderect(mp[4]):
            return "map16", 3, player.y

        if player.rect.colliderect(mp[8]):
            return "map24", 1509, player.y

        # update display
        pygame.display.flip()

    pygame.quit()
