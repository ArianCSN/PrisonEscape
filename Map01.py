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
    screen_width = 1536
    screen_height = 864
    pygame.display.set_caption('Prison Escape')
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

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

    # define player
    player = MyPlayer(x_pos, y_pos, screen, walk_up, walk_left, walk_down, walk_right, idle, 5, developer_mode)

    # define the bots
    bots = [Bot(200, 90, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(240, 480, screen, bot2_up, bot2_left, bot2_down, bot2_right, bot2_idle, 1, developer_mode),
            Bot(630, 420, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(540, 750, screen, bot2_up, bot2_left, bot2_down, bot2_right, bot2_idle, 1, developer_mode),
            Bot(1320, 420, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(990, 230, screen, bot2_up, bot2_left, bot2_down, bot2_right, bot2_idle, 1, developer_mode)]

    # define the walls
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

    # hidden walls that change maps
    mp = [MapChanger(750, 0, 90, 2), MapChanger(1535, 360, 2, 90),
          MapChanger(750, 863, 90, 2), MapChanger(0, 360, 2, 90)]

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
            # if player collide bots it goes to game over screen and pass player position of map00 for new start
            if player.rect.colliderect(bot.rect):
                sound_effect = pygame.mixer.Sound('assets/map01/sound/lose.wav')
                sound_effect.set_volume(0.2)
                sound_effect.play()
                pygame.mixer.music.stop()
                return "game_over", 780, 390

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
            return "map03", player.x, player.y

        if player.rect.colliderect(mp[2]):
            pass
            # return "04", 34, 321

        if player.rect.colliderect(mp[3]):
            pass
            # return "04", 34, 321

        # update display
        pygame.display.flip()

    pygame.quit()
