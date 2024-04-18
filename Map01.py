import pygame
from Ground import Ground
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from MapChanger import MapChanger


def map01(x_pos, y_pos, developer_mode):
    # start the pygame and pygame mixer
    pygame.init()
    pygame.mixer.init()

    # set up screen
    screen_width = 800
    screen_height = 600
    pygame.display.set_caption('Prison Escape')
    screen = pygame.display.set_mode((screen_width, screen_height))

    # load music
    pygame.mixer.music.load('assets/map01/sound/music.wav')
    # adjust the music volume to 0.4
    pygame.mixer.music.set_volume(0.4)
    # loop the music
    pygame.mixer.music.play(-1)

    # load textures
    ground_texture = pygame.image.load('assets/map01/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map01/wall/grey_bricks.jpg')

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

    # define player
    player = MyPlayer(x_pos, y_pos, screen, walk_up, walk_left, walk_down, walk_right, idle, 5, developer_mode)

    # define the bots
    bots = [Bot(200, 300, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(600, 300, screen, bot2_up, bot2_left, bot2_down, bot2_right, bot2_idle, 1, developer_mode),
            Bot(200, 300, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(600, 300, screen, bot2_up, bot2_left, bot2_down, bot2_right, bot2_idle, 1, developer_mode)]

    # define the walls
    walls = [Wall(0, 0, 150, 250, wall_texture), Wall(300, 0, 300, 200, wall_texture),
             Wall(600, 0, 200, 80, wall_texture), Wall(760, 230, 40, 170, wall_texture),
             Wall(650, 400, 200, 200, wall_texture), Wall(340, 525, 160, 75, wall_texture),
             Wall(0, 400, 150, 200, wall_texture)]

    # hidden walls that change maps
    mp = [MapChanger(150, 1, 150, 1), MapChanger(799, 80, 1, 150), MapChanger(500, 599, 150, 1),
          MapChanger(150, 599, 190, 1), MapChanger(0, 250, 1, 150)]

    # main loop of the map
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
        player.move(key)

        # Draw the walls
        for wall in walls:
            wall.draw(screen)

        # Draw the bots
        for bot in bots:
            bot.move()
            bot.check_collision(walls)
            bot.check_collision(mp)
            # if player collide bots it goes to game over screen and pass player position of map00 for new start
            if player.rect.colliderect(bot.rect):
                sound_effect = pygame.mixer.Sound('assets/map01/sound/lose.wav')
                sound_effect.set_volume(0.2)
                sound_effect.play()
                pygame.mixer.music.stop()
                return "game_over", 390, 435

        # player collide check with walls
        player.check_collision(walls)

        # options for developer mode
        # show position of mouse on screen
        # show player and bots rect and also hidden map changer with blue color
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            coord_text = font.render(f'X: {x}, Y: {y}', True, (255, 0, 0))
            screen.blit(coord_text, (10, 10))  # Draw the text

            player.draw_rect(screen)
            for bot in bots:
                bot.draw_rect(screen)
            for mp_dev in mp:
                mp_dev.draw(screen)

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[0]):
            return "map02", player.x, 545

        if player.rect.colliderect(mp[1]):
            pass
            # return "03", 34, 321

        if player.rect.colliderect(mp[2]):
            pass
            # return "04", 34, 321

        if player.rect.colliderect(mp[3]):
            pass
            # return "04", 34, 321

        if player.rect.colliderect(mp[4]):
            # return "05", 34, 321
            pass

        # update display
        pygame.display.flip()

    pygame.quit()
